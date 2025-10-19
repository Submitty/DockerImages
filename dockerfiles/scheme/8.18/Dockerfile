FROM ubuntu:22.04

# Install necessary packages for Scheme
RUN apt-get update \
    && apt-get -y install racket --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

CMD ["/bin/bash"]