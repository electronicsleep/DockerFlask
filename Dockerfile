FROM debian:stable

MAINTAINER Chris Robertson https://github.com/electronicsleep

RUN mkdir -p /usr/src/app
RUN apt-get update && apt-get install python-pip -y
RUN apt-get install redis-server -y
RUN pip install Flask Flask-Redis
RUN export FLASK_APP=Main.py

ADD Main.py /usr/src/app
ADD static /usr/src/app/static
ADD templates /usr/src/app/templates
ADD docker-redis-flask.sh /usr/src/app

WORKDIR /usr/src/app
EXPOSE 5000

#Run only Flask inside container
#CMD ["python", "Main.py"]

#Run Redis/Flask inside container
CMD ["bash", "docker-redis-flask.sh"]
