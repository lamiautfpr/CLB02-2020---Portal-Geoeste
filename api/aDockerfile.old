FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_ENV production

ENV FLASK_APP=run.py

EXPOSE 5000

CMD ["gunicorn", "-b",":5000", "run:app"]
