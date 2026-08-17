FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install common data science and clustering libraries, more such can be added as per needs later on
RUN pip3 install --no-cache-dir \
    numpy==2.2.6 \
    pandas==2.3.3 \
    scikit-learn==1.7.2 \
    scipy==1.15.3 

RUN ln -s /usr/bin/python3 /usr/bin/python
