DockerImages
============

This repo holds the various bits and scripts that help us to build the "official" Submitty
Docker images to be used for autograding. Each image is made up of some number of "components"
(Python 3.6, Clang 5, etc.) that only generate necessary artifacts that don't bring in unrelated
dependencies.

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
that builds the image and then pushes it to https://hub.docker.com.