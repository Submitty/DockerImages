FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y wget tar make
RUN wget https://www.php.net/distributions/php-7.4.33.tar.gz --no-check-certificate
RUN tar xzf php-7.4.33.tar.gz
RUN cd php-7.4.33
RUN apt-get update
# RUN apt-get --assume-yes install gcc
RUN apt-get -y install expect
RUN apt-get -y install pkg-config
RUN apt-get --assume-yes install -y libsqlite3-dev
RUN apt-get --assume-yes install -y libxml2-dev
RUN ./php-7.4.33/configure
RUN make
RUN make install

CMD ["/bin/bash"]

