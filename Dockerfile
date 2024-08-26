FROM python:3.8-slim-buster

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY config.py .

RUN pip install -r requirements.txt

CMD [ "python", "-u", "./main.py" ]