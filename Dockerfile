FROM node:6.11-wheezy

MAINTAINER Chris Robertson https://github.com/electronicsleep

RUN mkdir -p /usr/src/app
RUN apt-get update && apt-get install python-pip -y
RUN pip install Flask
RUN export FLASK_APP=Main.py

ADD Main.py /usr/src/app
ADD static /usr/src/app/static
ADD templates /usr/src/app/templates

WORKDIR /usr/src/app
EXPOSE 5000
CMD ["python", "Main.py"]
