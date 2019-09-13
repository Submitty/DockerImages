FROM debian:stretch-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        dirmngr \
        gnupg2 \
        wget \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 2EAF8B8BB12873F5 \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA3CBA3FFE22B574 \
    && echo "deb http://downloads.haskell.org/debian stretch main" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        emacs \
        cabal-install-3.0 \
        emacsen-common \
        ghc-8.8.1 \
        tk-dev \
    && update-alternatives --config opt-ghc \
    && update-alternatives --config opt-cabal \
    && wget -qO- https://get.haskellstack.org/ | sh \
    && ln -s /opt/ghc/bin/ghc /usr/bin/ghc \
    && ln -s /opt/ghc/bin/cabal /usr/bin/cabal \
    && ln -s /usr/local/bin/stack /usr/bin/stack \
    && wget https://github.com/mozart/mozart2/releases/download/v2.0.1/mozart2-2.0.1-x86_64-linux.deb -O /tmp/mozart.deb \
    && dpkg -i /tmp/mozart.deb \
    && apt-get install -f \
    && rm -rf /tmp/mozart.deb \
    && apt-get purge --auto-remove -y \
        ca-certificates \
        dirmngr \
        gnupg2 \
        wget \
    && rm -rf /var/lib/apt/lists/*
