DockerImages
============

This repo holds the various bits and scripts that help us to build the "official" Submitty
Docker images to be used for autograding. Each image is made up of some number of "components"
(Python 3.6, Clang 5, etc.) that only generate necessary artifacts that don't bring in unrelated
dependencies.


Adding Components
=================

Each image is made up of some number of 