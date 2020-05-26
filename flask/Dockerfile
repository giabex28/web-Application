#Use the Python3.6.9 container image
FROM python:3.6.9-stretch

#Set the working directory to /app
WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]



