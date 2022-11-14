#!bin/bash

cd `dirname $0`
cd ..

git add .
git commit -m $1
git push origin main