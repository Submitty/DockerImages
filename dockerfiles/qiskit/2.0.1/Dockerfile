FROM ubuntu:22.04

RUN apt-get update

RUN apt-get install python3.10 pip -y

RUN pip install --upgrade pip==22.0.2

RUN pip install qiskit[all]==2.0.1 notebook==7.4.3 qiskit-ibm-runtime==0.39.0
