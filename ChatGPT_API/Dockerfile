# syntax=docker/dockerfile:1
FROM python:3.11
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --user
COPY . .
CMD ["python", "./gpt_api.py"]