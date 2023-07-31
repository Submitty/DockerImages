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
# see CA_CERTIFICATES_JAVA_VERSION notes above
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure
ENV SUBMITTY_INSTALL_DIR /usr/local/submitty
ENV JUNIT_VERSION 4.12
ENV HAMCREST_VERSION 1.3
ENV JACOCO_VERSION 0.8.0


# Create the necessary directories
RUN mkdir -p ${SUBMITTY_INSTALL_DIR}/java_tools/JUnit \
  && mkdir -p ${SUBMITTY_INSTALL_DIR}/java_tools/hamcrest \
  && mkdir -p ${SUBMITTY_INSTALL_DIR}/java_tools/jacoco 

# Get JUnit
RUN apt-get update \
  && apt-get install -y --no-install-recommends wget \
  && rm -rf /var/lib/apt/lists/* \
  && echo 0 \
  && cd ${SUBMITTY_INSTALL_DIR}/java_tools/JUnit \
  && wget https://repo1.maven.org/maven2/junit/junit/${JUNIT_VERSION}/junit-${JUNIT_VERSION}.jar -o /dev/null > /dev/null 2>&1 \
  && cd / \
  && apt-get purge -y --auto-remove wget

# Get Hamcrest
RUN apt-get update \
  && apt-get install -y --no-install-recommends wget \
  && rm -rf /var/lib/apt/lists/* \
  && cd ${SUBMITTY_INSTALL_DIR}/java_tools/hamcrest \
  && wget https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/${HAMCREST_VERSION}/hamcrest-core-${HAMCREST_VERSION}.jar -o /dev/null > /dev/null 2>&1 \
  && cd / \
  && apt-get purge -y --auto-remove wget

# Get Jacoco
RUN apt-get update \
  && apt-get install -y --no-install-recommends wget unzip \
  && rm -rf /var/lib/apt/lists/* \
  && cd ${SUBMITTY_INSTALL_DIR}/java_tools/jacoco  \
  && wget https://github.com/jacoco/jacoco/releases/download/v${JACOCO_VERSION}/jacoco-${JACOCO_VERSION}.zip -o /dev/null > /dev/null 2>&1 \
  && mkdir jacoco-${JACOCO_VERSION} \
  && unzip jacoco-${JACOCO_VERSION}.zip -d jacoco-${JACOCO_VERSION} > /dev/null \
  && mv jacoco-${JACOCO_VERSION}/lib/jacococli.jar jacococli.jar \
  && mv jacoco-${JACOCO_VERSION}/lib/jacocoagent.jar jacocoagent.jar \
  && rm -rf jacoco-${JACOCO_VERSION} \
  && rm -f jacoco-${JACOCO_VERSION}.zip \
  && chmod o+r . *.jar \
  && cd / \
  && apt-get purge -y --auto-remove wget unzip

# Retrieve the Submitty Testrunner.
# TODO: replace this with something more sustainable than a wget from master
RUN apt-get update \
  && apt-get install -y --no-install-recommends wget \
  && rm -rf /var/lib/apt/lists/* \
  && wget https://raw.githubusercontent.com/Submitty/Submitty/master/junit_test_runner/TestRunner.java --output-document=${SUBMITTY_INSTALL_DIR}/java_tools/JUnit/TestRunner.java \
  && cd ${SUBMITTY_INSTALL_DIR}/java_tools/JUnit/ \
  && /usr/bin/javac -cp ./junit-4.12.jar TestRunner.java \
  && cd / \
  && apt-get purge -y --auto-remove wget


# Fix Permissions
RUN chown -R root:${COURSE_BUILDERS_GROUP} ${SUBMITTY_INSTALL_DIR}/java_tools \
  && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/java_tools


ENV MONO_VERSION 6.8.0.96

RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg \
    ca-certificates \
    wget \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https \
    dirmngr \
  && rm -rf /var/lib/apt/lists/* \
  && echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic/snapshots/6.12.0 main" | tee /etc/apt/sources.list.d/mono-official.list \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && apt-get update && apt-get install -y --no-install-recommends \
    mono-devel \
    msbuild \
  && rm -rf /var/lib/apt/lists/* /tmp/*

ENV DAFNY_VER v2.3.0
ENV DAFNY_FILE dafny-2.3.0.10506-x64-debian-8.11.zip
ENV SUBMITTY_INSTALL_DIR /usr/local/submitty

RUN apt-get update \
  && apt-get install -y --no-install-recommends wget unzip \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p ${SUBMITTY_INSTALL_DIR}/Dafny \
  && chown root:${COURSE_BUILDERS_GROUP} ${SUBMITTY_INSTALL_DIR}/Dafny \
  && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/Dafny \
  && cd ${SUBMITTY_INSTALL_DIR}/Dafny \
  && wget https://github.com/Microsoft/dafny/releases/download/${DAFNY_VER}/${DAFNY_FILE} \
  && unzip $DAFNY_FILE \
  && rm -f $DAFNY_FILE  \
  && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/Dafny \
  && cd / \
  && apt-get purge -y --auto-remove wget unzip

# dafny requires libgomp1
RUN apt-get update \
  && apt-get install -y libgomp1 \
  && rm -rf /var/lib/apt/lists/* CMD ["/bin/bash"]
