FROM ubuntu:22.04

# installing clang & clang++
RUN apt-get update
RUN apt-get install -y clang-14 lld-14

# for debugging system call filtering
RUN apt-get install -y strace

RUN rm -rf /var/lib/apt/lists/*

# symlinks
RUN ln -s /usr/bin/clang++-14 /usr/bin/clang++
RUN ln -s /usr/bin/clang-14 /usr/bin/clang
