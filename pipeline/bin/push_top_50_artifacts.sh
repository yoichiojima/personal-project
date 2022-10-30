#!bin/bash

PROJECT=yo-personal-project
REPOSITORY=yoichiojima
IMAGE=download-global-top-50

TAG=us-central1-docker.pkg.dev/$PROJECT/$REPOSITORY/$IMAGE

docker build -f "./pipeline/docker/Dockerfile" \
             -t $TAG \
             .

docker push $TAG