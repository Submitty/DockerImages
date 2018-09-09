#!/usr/bin/env python3

from argparse import ArgumentParser
import json
from pathlib import Path
import subprocess
import sys


def parse_args():
    parser = ArgumentParser()
    return parser.parse_args()


def enter_dir(path):
    for entry in path.iterdir():
        if entry.is_dir():
            enter_dir(entry)
        elif entry.is_file() and entry.name == "metadata.json":
            with entry.open() as open_file:
                metadata = json.load(open_file)
                tag = f"{metadata['hostname']}/{metadata['name']}:{metadata['tag']}"
                cmd = ['python3', 'dockerize.py', tag, *metadata['components']]
                subprocess.run(cmd, stdout=sys.stdout)


def main():
    args = parse_args()
    enter_dir(Path('dockerfiles'))


if __name__ == "__main__":
    main()