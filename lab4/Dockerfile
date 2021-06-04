FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /locallibrary
WORKDIR /locallibrary
COPY requirements.txt /locallibrary/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /locallibrary/
