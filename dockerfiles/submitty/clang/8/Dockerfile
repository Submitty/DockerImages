FROM debian:stretch-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update \
  && apt-get install -y --no-install-recommends wget gnupg \
  && echo "deb http://apt.llvm.org/stretch/ llvm-toolchain-stretch-8 main" >> /etc/apt/sources.list \
  && echo "deb-src http://apt.llvm.org/stretch/ llvm-toolchain-stretch-8 main" >> /etc/apt/sources.list \
  && wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add - \
  && apt-get update \
  && apt-get -y --no-install-recommends install \
    clang-8 \
  && apt-get -y install cmake\
  && apt-get -y install make\
  && apt-get purge -y --auto-remove wget gnupg \
  && rm -rf /var/lib/apt/lists/* \
  && ln -s /usr/bin/clang-8 /usr/bin/clang \
  && ln -s /usr/bin/clang++-8 /usr/bin/clang++
CMD ["/bin/bash"]
