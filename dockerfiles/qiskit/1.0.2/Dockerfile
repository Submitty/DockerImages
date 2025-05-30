FROM ubuntu:22.04

RUN apt-get update
# Python 3.10 is current version on apt-get as of 03/2024
RUN apt-get install python3.10 pip -y

RUN pip install --upgrade pip==22.0.2

RUN pip install qiskit[all]==1.0.2 notebook==7.4.3  qiskit-ibm-runtime==0.22.0
