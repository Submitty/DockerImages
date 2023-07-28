FROM debian:buster-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
      grep \
      libseccomp-dev \
      libseccomp2 \
      procps \
    && rm -rf /var/lib/apt/lists/*
RUN echo "deb http://ftp.debian.org/debian buster-backports main" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
      clang-6.0 \
    && apt-get -y install cmake\
    && apt-get -y install make\
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/clang-6.0 /usr/bin/clang \
    && ln -s /usr/bin/clang++-6.0 /usr/bin/clang++
RUN apt-get update \
    && apt-get install -y --no-install-recommends  g++ \
    && rm -rf /var/lib/apt/lists/*


ENV DRMEMORY_TAG release_2.5.0
ENV DRMEMORY_VERSION 2.5.0
ENV SUBMITTY_INSTALL_DIR /usr/local/submitty

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget ca-certificates rsync \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/drmemory \
    && cd /tmp \
    && wget https://github.com/DynamoRIO/drmemory/releases/download/${DRMEMORY_TAG}/DrMemory-Linux-${DRMEMORY_VERSION}.tar.gz \
    && tar -xpzf DrMemory-Linux-${DRMEMORY_VERSION}.tar.gz \
    && rsync --delete -a /tmp/DrMemory-Linux-${DRMEMORY_VERSION}/ ${SUBMITTY_INSTALL_DIR}/drmemory \
    && rm -rf /tmp/DrMemory* \
    && chown -R root ${SUBMITTY_INSTALL_DIR}/drmemory \
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/drmemory \
    && apt-get purge -y --auto-remove wget \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y valgrind \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y imagemagick \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y time \
    && rm -rf /var/lib/apt/lists/*

ENV AnalysisTools_Version v.18.06.00
ENV SUBMITTY_INSTALL_DIR /usr/local/submitty

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/count" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/count \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/plagiarism" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/plagiarism \
    && wget -nv "https://github.com/Submitty/AnalysisTools/releases/download/${AnalysisTools_Version}/diagnostics" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools/diagnostics \
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisTools \
    && apt-get purge -y --auto-remove wget \
    && rm -rf /var/lib/apt/lists/*


ENV AnalysisToolsTS_Version v23.06.01
ENV SUBMITTY_INSTALL_DIR /usr/local/submitty

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget \
    && mkdir -p ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build \
    && wget -nv "https://github.com/Submitty/AnalysisToolsTS/releases/download/${AnalysisToolsTS_Version}/submitty_count_ts" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build/submitty_count_ts \
    && wget -nv "https://github.com/Submitty/AnalysisToolsTS/releases/download/${AnalysisToolsTS_Version}/submitty_diagnostics_ts" -O ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS/build/submitty_diagnostics_ts \
    && chmod -R 755 ${SUBMITTY_INSTALL_DIR}/SubmittyAnalysisToolsTS \
    && apt-get purge -y --auto-remove wget \
    && rm -rf /var/lib/apt/lists/*
CMD ["/bin/bash"]
