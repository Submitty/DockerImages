FROM ubuntu:22.04

WORKDIR /usr/src/app
ENV LANG=C.UTF-8

# Set up the environment to be non-interactive for apt
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    libncurses5 libsctp1 \
    ca-certificates wget; \
    rm -rf /var/lib/apt/lists/*

# Download and install Erlang
RUN wget -O erlang.deb https://binaries2.erlang-solutions.com/ubuntu/pool/contrib/e/esl-erlang/esl-erlang_26.0-1~ubuntu~jammy_amd64.deb \
    && dpkg -i erlang.deb \
    && rm erlang.deb

# Default command
CMD ["/bin/bash"]
