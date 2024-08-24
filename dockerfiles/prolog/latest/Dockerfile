FROM debian:bullseye-slim

# Install necessary packages for SWI-Prolog
RUN apt-get update \
    && apt-get -y --no-install-recommends install \
    build-essential \
    curl \
    libgmp-dev \
    libssl-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install SWI-Prolog
RUN apt-get update \
    && apt-get install -y swi-prolog \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

CMD ["/bin/bash"]
