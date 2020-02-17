FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /vietnamracing
WORKDIR /vietnamracing
ADD requirements.txt /vietnamracing/
RUN pip install -r requirements.txt
ADD . /vietnamracing/