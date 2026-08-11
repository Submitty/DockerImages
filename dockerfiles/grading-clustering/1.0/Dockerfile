FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install common data science and clustering libraries, more such can be added as per needs later on
RUN pip3 install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    scipy 

RUN ln -s /usr/bin/python3 /usr/bin/python
