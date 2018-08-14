#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
import os

import docker

def parse_args():
    parser = ArgumentParser(description='Generate a Docker image from selected components')
    parser.add_argument('tag', type=str)
    parser.add_argument('component', nargs='+')
    return parser.parse_args()

def main():
    docker_client = docker.from_env()
    args = parse_args()
    if 'grep' not in args.component:
        args.component += ['core']
    with open('tmp/Dockerfile', 'w') as dockerfile:
        dockerfile.write("FROM alpine:3.8\n\n")
        for component in args.component:
            with Path('components', component, 'Dockerfile.part').open() as component_dockerfile:
                dockerfile.write(component_dockerfile.read() + "\n\n")
        # we need the " character around the command or else it doesn't work properly
        dockerfile.write("CMD [\"/bin/sh\"]\n")
    i,log = docker_client.images.build(path='tmp', tag=args.tag)
    for line in log:
        print(log)

if __name__ == '__main__':
    main()