# FROM python:3.6
FROM python:2.7

LABEL Name=Jeeves

LABEL Version=0.0.1

MAINTAINER Stephan Rayner <stephan.rayner@gmail.com>

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD python /code/main.py