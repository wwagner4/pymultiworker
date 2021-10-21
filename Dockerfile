FROM python:3.8

RUN python -m pip install --upgrade pip
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY *.py ./
