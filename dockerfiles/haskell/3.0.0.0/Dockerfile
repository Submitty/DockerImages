FROM ubuntu:22.04

# Install necessary dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    apt-utils curl build-essential libffi-dev libffi8 libgmp10 \
    libgmp-dev libncurses-dev libncurses5 libtinfo5 pkg-config \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install GHCup (Haskell toolchain manager)
RUN curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | bash -s -- -y

# Add GHCup to the PATH
ENV PATH="/root/.ghcup/bin:${PATH}"

# Install GHC 8.8.4 and Cabal using GHCup
RUN ghcup install ghc 8.8.4 \
    && ghcup set ghc 8.8.4 \
    && ghcup install cabal \
    && cabal update

WORKDIR /usr/src/app

CMD ["/bin/bash"]
