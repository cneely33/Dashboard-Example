# syntax=docker/dockerfile:1.2
### Example Docker file to create Dockerized version of DB for AWS hosting
FROM python:3.9.7

WORKDIR /app

## Copy requirements.txt
COPY Dashboard-Example/requirements.txt .
RUN pip install -r requirements.txt

## copy dashboard files over
COPY Dashboard-Example .
## copy required modules over 
COPY mods/ mods/

## expose port where dash is running
ENV PORT 8080
EXPOSE $PORT

## dont put secrets in Dockerfile
# ENV SECRET_KEY %set this key in secrets file%

## optional extranl data store; dont put secret in Dockerfile
# ENV SECRET_KEY 'config in aws'
# ENV aws_access_key_id 'config in aws'
# ENV aws_secret_access_key 'config in aws'
# ENV DATABASE_URI 'AWS RDS datastore'

ENV PYTHONUNBUFFERED=1

CMD gunicorn --workers=3 --threads=1 -b 0.0.0.0:$PORT index:server