#!bin/bash

PROJECT=yo-personal-project
REPOSITORY=yoichiojima
IMAGE=download-global-top-50

TAG=us-central1-docker.pkg.dev/$PROJECT/$REPOSITORY/$IMAGE

gcloud beta run jobs create download-global-top-50 --image $TAG \
                                                   --region us-central1