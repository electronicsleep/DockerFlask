#!/bin/bash
docker rm flaskapp
docker build -t flaskapp .
docker run -p 5000:5000 --name flaskapp -i -t flaskapp
