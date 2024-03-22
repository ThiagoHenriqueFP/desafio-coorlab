#!/bin/bash

echo "instaling backend dependencies"

pip install fastapi
pip install "uvicorn[standard]"
pip install pandas

echo "starting backend"

sh ./back.sh &

echo "instaling frontend dependencies"

cd app/frontend

yarn install

echo "starting frontend"

cd frontend

yarn serve