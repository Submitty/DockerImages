FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
# 2021 is the current version of texlive on apt-get as of 10/2024
RUN apt-get install -qqy texlive-latex-base=2021.20220204-1 texlive-plain-generic=2021.20220204-1 texlive-latex-extra=2021.20220204-1
RUN apt-get install -qqy python3.10 pip

RUN pip install PyPDF2==3.0.1