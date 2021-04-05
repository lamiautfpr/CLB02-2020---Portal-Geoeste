FROM gcr.io/google-appengine/python

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

FROM python:3.8-slim-buster

RUN python3 -m venv /opt/venv

# Install dependencies:
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

# Run the application:
COPY manage.py .
CMD . /opt/venv/bin/activate && exec python manage.py runserver