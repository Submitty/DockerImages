FROM debian:stable-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install OpenJDK 11 from AdoptOpenJDK
RUN curl -L -o /adoptopenjdk.tar.gz https://github.com/AdoptOpenJDK/openjdk11-upstream-binaries/releases/download/jdk-11.0.12%2B7/OpenJDK11U-jdk_x64_linux_11.0.12_7.tar.gz && \
    tar -xzf /adoptopenjdk.tar.gz -C /opt && \
    rm /adoptopenjdk.tar.gz && \
    ln -s /opt/jdk-11.0.12+7 /opt/openjdk11

# Set environment variables
ENV JAVA_HOME=/opt/openjdk11
ENV PATH=$JAVA_HOME/bin:$PATH

CMD ["/bin/bash"]
