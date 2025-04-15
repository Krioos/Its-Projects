FROM python:3.11.11

COPY python_requirments.txt /
RUN pip install -r python_requirments.txt

RUN mkdir /app
COPY app.py /app
WORKDIR /app