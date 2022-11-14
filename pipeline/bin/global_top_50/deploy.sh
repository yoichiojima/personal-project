#!bin/bash

PROJECT=yo-personal-project
REPOSITORY=yoichiojima
IMAGE=download-global-top-50
TAG=us-central1-docker.pkg.dev/$PROJECT/$REPOSITORY/$IMAGE


cd `dirname $0`
cd ../../../


docker build -f "./pipeline/docker/$IMAGE/Dockerfile" \
             -t $TAG \
             .
docker push $TAG


gcloud beta run jobs create $IMAGE \
    --image $TAG \
    --region us-central1


gcloud scheduler jobs create http $IMAGE \
  --location us-central1 \
  --schedule="0 0 * * *" \
  --uri="https://us-central1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/$PROJECT/jobs/$JOB:run" \
  --http-method POST \
  --oauth-service-account-email 9116302572-compute@developer.gserviceaccount.com