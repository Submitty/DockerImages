FROM ubuntu:22.04


WORKDIR /usr/src/app
ENV LANG C.UTF-8

# Install necessary build dependencies
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        wget \
        gcc \
        make \
        autoconf \
        libssl-dev \
        libncurses5-dev \
        libwxgtk3.0-gtk3-dev \
        libgl1-mesa-dev \
        libglu1-mesa-dev \
        libpng-dev \
        libssh-dev \
        unixodbc-dev \
        xsltproc \
        fop \
        git \
    ; \
    rm -rf /var/lib/apt/lists/*

# Set Erlang version and URL for the tarball
ENV ERLANG_VERSION OTP-26.0
ENV ERLANG_DOWNLOAD_URL https://api.github.com/repos/erlang/otp/tarball/refs/tags/$ERLANG_VERSION

# Download and install Erlang/OTP from source
RUN set -eux; \
    wget -O erlang.tar.gz $ERLANG_DOWNLOAD_URL; \
    mkdir -p /usr/src/erlang; \
    tar -xzf erlang.tar.gz --strip-components=1 -C /usr/src/erlang; \
    rm erlang.tar.gz; \
    cd /usr/src/erlang; \
    ./otp_build autoconf; \
    ./configure --without-javac; \
    make -j$(nproc); \
    make install; \
    cd /; \
    rm -rf /usr/src/erlang

# Verify Erlang installation
RUN erl -version

CMD ["/bin/bash"]
