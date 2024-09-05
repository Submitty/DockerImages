FROM ubuntu:22.04

# Install necessary packages for GHC (compiler)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libgmp-dev \
    ghc cabal-install \
    && rm -rf /var/lib/apt/lists/*
    
# Maybe add Stack (another build tool for Haskell), up to Instructor?
# RUN curl -sSL https://get.haskellstack.org/ | sh

WORKDIR /usr/src/app

CMD ["/bin/bash"]