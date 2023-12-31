# syntax=docker/dockerfile:1.2
### Example Docker file to create Dockerized version of DB for AWS hosting
FROM python:3.9.7

WORKDIR /app

## Copy requirements.txt
COPY Dashboard/PC2/requirements.txt .
RUN pip install -r requirements.txt

## copy dashboard files over
COPY Dashboard/PC2 .
## copy required modules over
COPY mods/ mods/

ENV PORT 8080
EXPOSE $PORT

# ENV SECRET_KEY 'config in aws'
# ENV aws_access_key_id 'config in aws'
# ENV aws_secret_access_key 'config in aws'

ENV PYTHONUNBUFFERED=1

CMD gunicorn --workers=3 --threads=1 -b 0.0.0.0:$PORT index:server