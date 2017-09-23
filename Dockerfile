FROM python:3

ADD ./requirements.txt /
RUN pip install -r requirements.txt

ADD ./test /code
WORKDIR /code

ENTRYPOINT ["python"]
CMD ["consumer.py"]
