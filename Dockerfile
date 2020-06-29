FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV VERSION 0.0.1

ADD . .

RUN pip install pipenv && pipenv install

CMD ["pipenv", "run", "python", "main.py"]
