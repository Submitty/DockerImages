# Note: This Dockerfile represents the original "Ubuntu" build image
# that Submitty included inside the main repo. As such, it does
# not have the same conventions as the other images and does not have
# any metadata.json file or is made up of components parts. Have to edit
# this file directly.

FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y libpython3.10
RUN apt-get install -y python3-dev
RUN apt-get install -y clang lld lldb
RUN apt-get install -y gcc g++ 
#RUN apt-get install -y gdb

RUN apt-get install -y autoconf automake autotools-dev
RUN apt-get install -y diffstat
RUN apt-get install -y finger sed
RUN apt-get -y install locales

RUN apt-get install -y git
RUN apt-get install -y git-man 
RUN apt-get install -y dpkg-dev
RUN apt-get install -y p7zip-full
RUN apt-get install -y patchutils 
RUN apt-get install -y libpq-dev
RUN apt-get install -y unzip zip
#RUN apt-get install -y valgrind
RUN apt-get install -y libmagic-ocaml-dev 
RUN apt-get install -y javascript-common  
RUN apt-get install -y libfile-mmagic-perl libgnupg-interface-perl libbsd-resource-perl libarchive-zip-perl 
RUN apt-get install -y jq libseccomp-dev libseccomp2 seccomp
#RUN apt-get install -y junit
RUN apt-get install -y flex
RUN apt-get install -y bison
RUN apt-get install -y spim
RUN apt-get install -y poppler-utils
#RUN apt-get install -y imagemagick
RUN apt-get install -y cloc

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_CTYPE=en_US.UTF-8

ENV DRMEMORY_TAG release_2.6.0
ENV DRMEMORY_VERSION 2.6.0
ENV AnalysisTools_Version v22.03.00
ENV AnalysisToolsTS_Version v23.10.00
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
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS
    

RUN mkdir -p ${SUBMITTY_INSTALL_DIR}/bin
RUN wget -nv https://raw.githubusercontent.com/Submitty/Submitty/refs/heads/main/bin/comment_count.py -O ${SUBMITTY_INSTALL_DIR}/bin/comment_count.py
RUN chmod -R 755 ${SUBMITTY_INSTALL_DIR}/bin/
RUN chmod -R 755 ${SUBMITTY_INSTALL_DIR}/bin/comment_count.py

RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen

# for debugging system call filtering
RUN apt-get install -y strace

RUN apt-get purge -y --auto-remove wget
RUN rm -rf /var/lib/apt/lists/*




#RUN locale-gen
#RUN dpkg-reconfigure locales


