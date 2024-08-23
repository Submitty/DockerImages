FROM debian:bullseye-slim

# Install necessary packages for GHC (compiler)
RUN apt-get update \
    && apt-get -y --no-install-recommends install \
    build-essential \
    curl \
    libgmp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install GHC/Cabal (build tool)
RUN apt-get update \
    && apt-get install -y ghc cabal-install \
    && rm -rf /var/lib/apt/lists/*

# Maybe add Stack (another build tool for Haskell), up to Instructor?
# RUN curl -sSL https://get.haskellstack.org/ | sh

WORKDIR /usr/src/app

CMD ["/bin/bash"]