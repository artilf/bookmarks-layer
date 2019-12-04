FROM amazonlinux:2017.09.1.20180409

WORKDIR /workdir
COPY requirements.txt ./
RUN yum install -y gcc python36 python36-devel python36-pip

ENTRYPOINT ["pip-3.6", "install", "-r", "requirements.txt", "-t", "./python"]
