#!bin/bash

cd /app/pipeline
python3 -m luigi --module job DownloadGlobalTop50 --local-scheduler