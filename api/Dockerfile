FROM amazonlinux:1

RUN yum -y install python38 python38-pip
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python3
RUN yum -y install python3-devel mysql-devel gcc
RUN pip install werkzeug==2.1.2
# Set the same WORKDIR as default image
RUN mkdir /var/task
COPY requirements.txt /var/task
WORKDIR /var/task



