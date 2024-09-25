# First Stage: Builder
FROM ubuntu:22.04 AS builder

# Set the working directory
WORKDIR /usr/src/app

# Install libgmp-dev explicitly for runtime linking
RUN apt-get update \
    && apt search cabal-install \
    && apt-get install -y --no-install-recommends \
    libgmp10 libtinfo5 build-essential libgmp-dev ghc=8.8.4-3 cabal-install=3.0.0.0-3build1.1 \
    && rm -rf /var/lib/apt/lists/*

# Default command to keep the container running
CMD ["/bin/bash"]
