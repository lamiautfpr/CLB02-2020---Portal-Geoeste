FROM gcr.io/google-appengine/python

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

FROM python:3.8-slim-buster

WORKDIR /portal

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["python", "manage.py", "runserver"]
