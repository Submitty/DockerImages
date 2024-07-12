FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y wget tar make
RUN wget https://www.php.net/distributions/php-7.4.33.tar.gz --no-check-certificate && \
    tar xzf php-7.4.33.tar.gz && \
    cd php-7.4.33
RUN apt-get update && \
    apt-get --assume-yes install gcc && \
    apt-get -y install expect && \
    apt-get -y install pkg-config && \
    apt-get --assume-yes install -y libsqlite3-dev && \
    apt-get --assume-yes install -y libxml2-dev
RUN ./php-7.4.33/configure
RUN make && \
    make install

CMD ["/bin/bash"]

