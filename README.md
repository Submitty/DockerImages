DockerImages
============

This repo holds the various bits and scripts that help us to build the "official" Submitty
Docker images to be used for autograding. Each image is made up of some number of "components"
(Python 3.6, Clang 5, etc.) that only generate necessary artifacts that don't bring in unrelated
dependencies.

To report issues for this repository, please file them under the [Submitty/Submitty](https://github.com/Submitty/Submitty) repository.

Requirements
============
* Python 3.6+
* [Docker](https://www.docker.com)
* [docker-python](https://pypi.org/project/docker/) (`pip install docker`)

It's recommended to use [pipenv](https://pipenv.readthedocs.io/en/latest/) and the included Pipfile.


Usage
=====
The repo has several scripts with different purposes. To get help with any of them, use the `--help`
flag.

dockerize.py
------------
```
$ ./dockerize.py --help
usage: dockerize.py [-h] [--base BASE] [--build]
                    tag [component [component ...]]

Generate a Dockerfile from components.

positional arguments:
  tag                   Tag to use for the generated dockerfile. Format should
                        be {hostname}/{name}:{tag} and used for pushing to
                        Docker Hub.
  component             Components to include into the Dockerfile. Format for
                        the component is the path to the Dockerfile.part file
                        (ex: python/3.6.6

optional arguments:
  -h, --help            show this help message and exit
  --base BASE, -b BASE  Base image to use for the Dockerfile (default:
                        debian:stretch-slim)
  --build               Build the generated dockerfile (default: false)
```

regenerate.py
----------
```
$ ./regenerate.py --help
usage: regenerate.py [-h]

Goes through all generated Dockerfiles, taking in the associated metadata.json
for each and re-run dockerize.py to regenerate the Dockerfile.

optional arguments:
  -h, --help  show this help message and exit
```

trigger.py
----------
```
$ ./trigger.py --help
usage: trigger.py [-h]

Adds a newline to all generated Dockerfiles so one can do a git commit with
all the files and trigger Travis-CI to run.

optional arguments:
  -h, --help  show this help message and exit
```

Publishing Images
=================

After running the `dockerize.py` script, it writes the generated `Dockerfile` to a folder within
`dockerfiles` based on the tag name you provided the script. For example, if you use the tag
`submitty/python:3.6`, it will write a `Dockerfile` to `/dockerfiles/submitty/python/3.6/`.
Additionally, a `metadata.json` file will be created that has the following format:
```
{
  "hostname": "hostname of where to publish on hub (e.g. submitty)",
  "name": "name of the repo to publish to (e.g. python)",
  "tag": "tag of the image (e.g. 3.6)",
  "components": [
    "list",
    "of",
    "components",
    "(e.g. python/3.6.6)"
  ]
}
```

While you could build these images (or pass the `--build` flag to `dockerize.py`), anytime you commit
a `Dockerfile` and `metadata.json` pair under `dockerfiles` to GitHub, a Travis-CI build is kicked off
which builds the image and then pushes it to https://hub.docker.com.
