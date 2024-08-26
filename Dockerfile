FROM python:3.8-alpine

WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY config.py .

RUN pip install -r requirements.txt

CMD [ "python", "-u", "./main.py" ]