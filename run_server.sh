#!/bin/bash

source activate wrf_server

gunicorn -w 2 data:app -b 127.0.0.1:8000
