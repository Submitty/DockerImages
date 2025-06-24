FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y gcc-11 g++-11

# for debugging system call filtering
RUN apt-get install -y strace

RUN rm -rf /var/lib/apt/lists/*

# symlinks - x86
RUN if test -e /usr/bin/x86_64-linux-gnu-gcc-11; then ln -s /usr/bin/x86_64-linux-gnu-gcc-11 /usr/bin/gcc; fi
RUN if test -e /usr/bin/x86_64-linux-gnu-g++-11; then ln -s /usr/bin/x86_64-linux-gnu-g++-11 /usr/bin/g++; fi

# symlinks - ARM
RUN if test -e /usr/bin/aarch64-linux-gnu-gcc-11; then ln -s /usr/bin/aarch64-linux-gnu-gcc-11 /usr/bin/gcc; fi
RUN if test -e /usr/bin/aarch64-linux-gnu-g++-11; then ln -s /usr/bin/aarch64-linux-gnu-g++-11 /usr/bin/g++; fi
