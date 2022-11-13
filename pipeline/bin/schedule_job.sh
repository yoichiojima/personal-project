#!bin/bash

PROJECT=yo-personal-project
JOB=download-global-top-50

gcloud scheduler jobs create http download-global-top-50 \
  --location us-central1 \
  --schedule="0 0 * * *" \
  --uri="https://us-central1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/$PROJECT/jobs/$JOB:run" \
  --http-method POST \
  --oauth-service-account-email 9116302572-compute@developer.gserviceaccount.com