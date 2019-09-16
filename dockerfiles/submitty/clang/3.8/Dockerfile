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
      clang-3.8 \
    && apt-get -y install cmake\
    && apt-get -y install make\
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/clang-3.8 /usr/bin/clang \
    && ln -s /usr/bin/clang++-3.8 /usr/bin/clang++
CMD ["/bin/bash"]
