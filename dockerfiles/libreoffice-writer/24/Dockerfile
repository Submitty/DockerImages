FROM ubuntu:24.04

RUN apt-get update
RUN apt-get update --fix-missing
RUN apt-get install -y libreoffice-writer-nogui

# cleanup
RUN rm -rf /var/lib/apt/lists/*