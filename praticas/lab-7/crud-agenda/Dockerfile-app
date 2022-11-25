FROM python:3.9-alpine

WORKDIR /app

COPY source_code/ /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "server.py"]
