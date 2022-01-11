FROM python:3.8-slim-buster

WORKDIR  /app

COPY main.py main.py
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["echo","Hello World... from my first docker image"]
CMD ["python3","/app/main.py"]
