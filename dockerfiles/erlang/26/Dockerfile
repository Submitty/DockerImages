# Use the base image
FROM ubuntu:22.04

WORKDIR /usr/src/app
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV KERL_BASE_DIR=/usr/local/kerl

# Install dependencies for Erlang and the build process
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    build-essential \
    libncurses5-dev libsctp1 \
    ca-certificates wget curl git \
    autoconf m4 libssl-dev libwxgtk3.0-gtk3-dev libgl1-mesa-dev \
    libglu1-mesa-dev libpng-dev libssh-dev unixodbc-dev xsltproc fop \
    locales; \
    rm -rf /var/lib/apt/lists/*

# Install kerl to manage Erlang builds
RUN curl -O https://raw.githubusercontent.com/kerl/kerl/master/kerl && \
    chmod +x kerl && \
    mv kerl /usr/local/bin/kerl

# Update kerl releases and build Erlang 26.0
RUN kerl update releases
RUN MAKEFLAGS=-j6 kerl build 26.0 26.0_build
RUN kerl install 26.0_build /usr/local/erlang/26.0

# Cleanup the build files
RUN rm -rf /usr/local/kerl/builds/26.0_build

# Activate the Erlang environment by default
RUN echo ". /usr/local/erlang/26.0/activate" >> /root/.bashrc && \
    echo ". /usr/local/erlang/26.0/activate" >> /etc/profile

# Default command
CMD ["/bin/bash"]
