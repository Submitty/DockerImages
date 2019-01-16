FROM debian:stretch-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      clang-4.0 \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/clang-4.0 /usr/bin/clang \
    && ln -s /usr/bin/clang++-4.0 /usr/bin/clang++
CMD ["/bin/bash"]
