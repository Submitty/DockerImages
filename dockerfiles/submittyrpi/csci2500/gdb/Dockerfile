FROM debian:stretch-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update \
    && apt-get install -y --no-install-recommends  g++ \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y valgrind \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y --no-install-recommends  gdb \
    && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
