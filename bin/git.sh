#!bin/bash

echo `dirname "$0"`

git add .
git commit -m $1
git push origin main