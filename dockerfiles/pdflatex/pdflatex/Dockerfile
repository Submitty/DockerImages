FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -qqy texlive-latex-base texlive-latex-recommended texlive-plain-generic texlive-latex-extra
RUN apt-get install -qqy python3.10 pip

RUN pip3 install PyPDF2==3.0.1

RUN mkdir -p /var/local/submitty/autograding_tmp

WORKDIR /var/local/submitty/autograding_tmp