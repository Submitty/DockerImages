FROM debian:stretch-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
    && rm -rf /var/lib/apt/lists/*
#
# Source: https://github.com/docker-library/openjdk/blob/master/8/jdk/slim/Dockerfile
#

# A few reasons for installing distribution-provided OpenJDK:
#
#  1. Oracle.  Licensing prevents us from redistributing the official JDK.
#
#  2. Compiling OpenJDK also requires the JDK to be installed, and it gets
#     really hairy.
#
#     For some sample build times, see Debian's buildd logs:
#       https://buildd.debian.org/status/logs.php?pkg=openjdk-8

RUN apt-get update && apt-get install -y --no-install-recommends \
		bzip2 \
		unzip \
		xz-utils \
	&& rm -rf /var/lib/apt/lists/*

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home

# do some fancy footwork to create a JAVA_HOME that's cross-architecture-safe
RUN ln -svT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)" /docker-java-home
ENV JAVA_HOME /docker-java-home

# Look here to update: https://packages.debian.org/stretch/openjdk-8-jdk-headless
ENV JAVA_VERSION 8u232
ENV JAVA_DEBIAN_VERSION 8u232-b09-1~deb9u1

# see https://bugs.debian.org/775775
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872
# Look here to update: https://packages.debian.org/stretch/ca-certificates-java
ENV CA_CERTIFICATES_JAVA_VERSION 20170929~deb9u3

RUN set -ex; \
	\
# deal with slim variants not having man page directories (which causes "update-alternatives" to fail)
	if [ ! -d /usr/share/man/man1 ]; then \
		mkdir -p /usr/share/man/man1; \
	fi; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends \
		openjdk-8-jdk-headless="$JAVA_DEBIAN_VERSION" \
		ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \
	; \
	rm -rf /var/lib/apt/lists/*; \
	\
# verify that "docker-java-home" returns what we expect
	[ "$(readlink -f "$JAVA_HOME")" = "$(docker-java-home)" ]; \
	\
# update-alternatives so that future installs of other OpenJDK versions don't change /usr/bin/java
	update-alternatives --get-selections | awk -v home="$(readlink -f "$JAVA_HOME")" 'index($3, home) == 1 { $2 = "manual"; print | "update-alternatives --set-selections" }'; \
# ... and verify that it actually worked for one of the alternatives we care about
	update-alternatives --query java | grep -q 'Status: manual'

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

CMD ["/bin/bash"]
