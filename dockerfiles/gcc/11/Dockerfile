FROM ubuntu:22.04

# installing requirements to get and extract prebuilt binaries
RUN apt-get update
RUN apt-get install -y gcc-11 g++-11
RUN rm -rf /var/lib/apt/lists/*

# symlinks
RUN if test -e /usr/bin/aarch64-linux-gnu-gcc-11; then ln -s /usr/bin/aarch64-linux-gnu-gcc-11 /usr/bin/gcc; fi
RUN if test -e /usr/bin/aarch64-linux-gnu-g++-11; then ln -s /usr/bin/aarch64-linux-gnu-g++-11 /usr/bin/g++; fi
