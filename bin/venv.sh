#!bin/bash

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r ./notebook/requirements.txt
pip install -r ./pipeline/requirements.txt
pip install -r ./rest/requirements.txt