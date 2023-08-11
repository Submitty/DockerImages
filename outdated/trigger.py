#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path


def parse_args():
    description=(
        'Adds a newline to all generated Dockerfiles so one can do a git commit'
        ' with all the files and trigger Travis-CI to run.'
    )
    parser = ArgumentParser(description=description)
    return parser.parse_args()


def enter_dir(path):
    for entry in path.iterdir():
        if entry.is_dir():
            enter_dir(entry)
        elif entry.is_file() and entry.name == "Dockerfile":
            entry.write_text("\n")


def main():
    args = parse_args()
    enter_dir(Path('dockerfiles'))


if __name__ == "__main__":
    main()