FROM gcr.io/google-appengine/python

RUN apt-get update && apt-get install -y \
  binutils \
  gdal-bin \
  python-gdal

RUN virtualenv /env -p python3.6

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

CMD python ./manage.py runserver