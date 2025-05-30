FROM ubuntu:22.04

# DO NOT EXPOSE ANY PORTS IN THIS FILE

# Install necessary packages (Java and curl)
RUN apt-get update \
    && apt-get install -y openjdk-17-jdk curl --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN mkdir -p /usr/local/lib/salsa
ENV SALSA_JAR_SHA256=821fe5ec2922ff32f09fa55280afd023aa9852c7cc074f90cd086a4691e327af

# Download the Salsa compiler jar file
RUN curl -SL -o /usr/local/lib/salsa/salsa1.1.6.jar http://wcl.cs.rpi.edu/salsa/releases/salsa1.1.6.jar \
    && echo "$SALSA_JAR_SHA256  /usr/local/lib/salsa/salsa1.1.6.jar" | sha256sum -c -

RUN apt-get remove curl -y && apt autoremove -y && apt clean -y

# Set environment variable for the Salsa compiler jar location
ENV SALSA_COMPILER_JAR=/usr/local/lib/salsa/salsa1.1.6.jar
ENV SALSAOPTS=""

# Write aliases to a separate file
RUN echo "alias salsac='java -cp $SALSA_COMPILER_JAR:. salsac.SalsaCompiler *.salsa; javac -classpath $SALSA_COMPILER_JAR:. *.java'" >> /usr/src/app/salsa_aliases.sh && \
    echo "alias salsa='java -cp $SALSA_COMPILER_JAR:. $SALSAOPTS'" >> /usr/src/app/salsa_aliases.sh && \
    echo "alias wwcns='java -cp $SALSA_COMPILER_JAR:. wwc.naming.WWCNamingServer'" >> /usr/src/app/salsa_aliases.sh && \
    echo "alias wwctheater='java -cp $SALSA_COMPILER_JAR:. $SALSAOPTS wwc.messaging.Theater'" >> /usr/src/app/salsa_aliases.sh

# make sure the aliases script gets sourced on container start
RUN echo "source /usr/src/app/salsa_aliases.sh" >> /etc/bash.bashrc

CMD ["bash"]