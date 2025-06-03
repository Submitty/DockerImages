FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y wget

ARG TARGETARCH

ARG TARGETARCH
        RUN if [ "$TARGETARCH" = "amd64" ]; then \
            echo "Setting up for amd64"; \
        elif [ "$TARGETARCH" = "arm64" ]; then \
            echo "Setting up for arm64"; \
        fi

# x86 
RUN if [ $TARGETARCH = "amd64" ]; then \
  wget https://julialang-s3.julialang.org/bin/linux/x64/1.11/julia-1.11.5-linux-x86_64.tar.gz ; \
  tar zxvf julia-1.11.5-linux-x86_64.tar.gz ; \
  ln -s /julia-1.11.5/bin/julia /usr/bin/julia ; \
fi


# arm   
RUN if [ $TARGETARCH = "arm64" ]; then \
  wget https://julialang-s3.julialang.org/bin/linux/aarch64/1.11/julia-1.11.5-linux-aarch64.tar.gz ; \
  tar zxvf julia-1.11.5-linux-aarch64.tar.gz ; \
  ln -s /julia-1.11.5/bin/julia /usr/bin/julia ; \
fi

# for debugging system call filtering
RUN apt-get install -y strace

RUN rm -rf /var/lib/apt/lists/*