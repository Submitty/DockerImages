FROM ubuntu:22.04

# Install necessary packages for SWI-Prolog
RUN apt-get update \
    && apt-get -y install swi-prolog=8.4.2+dfsg-2ubuntu1 --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

CMD ["/bin/bash"]
