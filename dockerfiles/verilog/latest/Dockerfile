FROM debian:bullseye-slim

RUN apt-get update \
      && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
      && rm -rf "/var/lib/apt/lists/*"

RUN apt-get update \
    && apt-get install -y iverilog gtkwave \
    && rm -rf "/var/lib/apt/lists/*"

CMD ["/bin/bash"]
