# Note: This Dockerfile represents the original "Ubuntu" build image
# that Submitty included inside the main repo. As such, it does
# not have the same conventions as the other images and does not have
# any metadata.json file or is made up of components parts. Have to edit
# this file directly.

FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -qqy python python-dev python3 python3-dev libpython3.5
RUN apt-get install -qqy clang autoconf automake autotools-dev diffstat finger gdb git git-man \
    dpkg-dev p7zip-full patchutils \
    libpq-dev unzip valgrind zip libmagic-ocaml-dev \
    javascript-common  \
    libfile-mmagic-perl libgnupg-interface-perl libbsd-resource-perl libarchive-zip-perl gcc g++ \
    jq libseccomp-dev libseccomp2 seccomp junit flex bison spim poppler-utils
RUN apt-get install -qqy imagemagick

ENV DRMEMORY_TAG release_2.6.0
ENV DRMEMORY_VERSION 2.6.0
ENV AnalysisTools_Version v22.03.00
ENV AnalysisToolsTS_Version v23.06.01
ENV SUBMITTY_INSTALL_DIR /usr/local/submitty

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget ca-certificates rsync \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/drmemory \
    && cd /tmp \
    && wget https://github.com/DynamoRIO/drmemory/releases/download/${DRMEMORY_TAG}/DrMemory-Linux-${DRMEMORY_VERSION}.tar.gz \
    && tar -xpzf DrMemory-Linux-${DRMEMORY_VERSION}.tar.gz \
    && rsync --delete -a /tmp/DrMemory-Linux-${DRMEMORY_VERSION}/ ${SUBMITTY_INSTALL_DIR}/drmemory \
    && rm -rf /tmp/DrMemory* \
    && chown -R root:${COURSE_BUILDERS_GROUP} ${SUBMITTY_INSTALL_DIR}/drmemory \
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/drmemory \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/count" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/count \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/plagiarism" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/plagiarism \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/diagnostics" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/diagnostics \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build \
    && wget -nv "https://github.com/Submitty/AnalysisToolsTS/releases/download/${AnalysisToolsTS_Version}/submitty_count_ts" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build/submitty_count_ts \
    && wget -nv "https://github.com/Submitty/AnalysisToolsTS/releases/download/${AnalysisToolsTS_Version}/submitty_diagnostics_ts" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build/submitty_diagnostics_ts \
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS \
    && apt-get purge -y --auto-remove wget \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/local/submitty/autograding_tmp
#RUN mkdir -p /var/local/submitty/autograding_tmp/untrustedtmp/TMP_COMPILATION
#RUN mkdir -p /var/local/submitty/autograding_tmp/untrustedtmp/TMP_COMPILATION
#RUN mkdir -p /var/local/submitty/autograding_tmp/untrustedtmp/TMP_WORK

WORKDIR /var/local/submitty/autograding_tmp

# mount to /usr/src/app
