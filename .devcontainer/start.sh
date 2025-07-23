#!/bin/bash

./download_parquet.sh

uvicorn api:app --host=0.0.0.0 --port=10000