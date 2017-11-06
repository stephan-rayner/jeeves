FROM cheesemanor/base-python:latest
LABEL Author="Stephan Rayner <stephan.rayner@gmail.com>"
LABEL Name="Jeeves"
LABEL Version="0.0.1"
ADD . /code

WORKDIR /code

RUN pip3 install -r requirements.txt

CMD python3 /code/main.py
