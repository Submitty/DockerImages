FROM ubuntu:18.04
# Install "software-properties-common" (for the "add-apt-repository")
RUN apt-get update && apt-get install -y \
    software-properties-common
# Add the "JAVA" ppa
RUN add-apt-repository -y \
    ppa:openjdk-r/ppa

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

ENV SUBMITTY_INSTALL_DIR /usr/local/submitty

RUN apt-get update \
  && apt-get install -y --no-install-recommends curl \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p ${SUBMITTY_INSTALL_DIR}/java_tools/soot \
  && cd ${SUBMITTY_INSTALL_DIR}/java_tools/soot \
  && curl http://www.cs.rpi.edu/~milanova/soot-develop.jar > soot-develop.jar \
  && curl http://www.cs.rpi.edu/~milanova/rt.jar > rt.jar \
  && curl https://soot-build.cs.uni-paderborn.de/public/origin/develop/soot/soot-develop/build/sootclasses-trunk.jar > sootclasses-trunk.jar \
  && curl https://soot-build.cs.uni-paderborn.de/public/origin/develop/soot/soot-develop/build/sootclasses-trunk-jar-with-dependencies.jar > sootclasses-trunk-jar-with-dependencies.jar \
  && cd / \
  && chown -R root:${COURSE_BUILDERS_GROUP} ${SUBMITTY_INSTALL_DIR}/java_tools \
  && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/java_tools \
  && apt-get purge -y --auto-remove curl

CMD ["/bin/bash"]
