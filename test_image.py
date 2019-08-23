#!/usr/bin/env python3

import argparse
import docker


def main():
    parser = argparse.ArgumentParser(description="Test an image to use in Submitty")
    parser.add_argument("image", type=str, help="Image to test")
    args = parser.parse_args()

    client = docker.from_env()
    container = client.containers.run(
        args.image,
        auto_remove=True,
        detach=True,
        stdin_open=True
    )

    missing = []

    container.exec_run(cmd=['mkdir', '-p', '/tmp/test'])
    (code, result) = container.exec_run(
        cmd="/bin/bash -c 'echo \"test\" > /tmp/test/test.txt'"
    )
    (code, result) = container.exec_run(cmd="/bin/bash -c \"grep 'test' /tmp/**/*\"")
    if code != 0 or result.decode('utf-8').strip() != 'test':
        missing.append('grep')

    (code, result) = container.exec_run(
        cmd="find / -type f -name '*libseccomp*'"
    )
    if code != 0 or len(result.decode('utf-8').strip()) == 0:
        missing.append('seccomp')

    (code, result) = container.exec_run(cmd=["ps", "--version"])
    if code != 0 or not result.decode('utf-8').strip().startswith('ps from procps'):
        missing.append('procps')

    print(f"Validation of {args.image}...")
    if len(missing) == 0:
        print("  PASSED")
    else:
        print("  FAILED")
        print("  MISSING:")
        for item in missing:
            print(f"  -  {item}")


if __name__ == "__main__":
    main()
