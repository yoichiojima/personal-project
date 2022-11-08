#!bin/bash

gcloud scheduler jobs create http download_global_top_50 \
  --location us-central1 \
  --schedule="0 0 * * *" \
  --uri="https://us-central1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/yo-personal-project/jobs/download_global_top_50:run" \
  --http-method POST \
  --oauth-service-account-email 9116302572-compute@developer.gserviceaccount.com
