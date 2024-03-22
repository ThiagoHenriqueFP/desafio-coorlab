#!/bin/bash

cd ../
python3 -m uvicorn app.backend.main:app --reload --port 3000 || python -m uvicorn app.backend.main:app --reload --port 3000
