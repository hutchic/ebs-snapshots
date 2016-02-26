from ubuntu:14.04

RUN mkdir /src

RUN apt-get install -y software-properties-common \
  && apt-add-repository -y ppa:ansible/ansible \
  && apt-get update \
  && apt-get install -y ansible python-pip python-dateutil \
  && pip install boto

COPY . /src
WORKDIR /src
