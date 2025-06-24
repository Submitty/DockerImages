FROM ubuntu:22.04

# installing python
RUN apt-get update
RUN apt-get install -y python3.10

# for debugging system call filtering
RUN apt-get install -y strace

RUN rm -rf /var/lib/apt/lists/*

# symlinks
RUN ln -s /usr/bin/python3.10 /usr/bin/python3
