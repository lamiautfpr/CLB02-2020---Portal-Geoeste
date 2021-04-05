FROM gcr.io/google-appengine/python
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
FROM python:3.7.9-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "manage.py", "runserver"]