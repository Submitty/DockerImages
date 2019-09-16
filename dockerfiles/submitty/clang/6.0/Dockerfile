FROM debian:stretch-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
    && rm -rf /var/lib/apt/lists/*
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
      clang-6.0 \
    && apt-get -y install cmake\
    && apt-get -y install make\
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/clang-6.0 /usr/bin/clang \
    && ln -s /usr/bin/clang++-6.0 /usr/bin/clang++
CMD ["/bin/bash"]
