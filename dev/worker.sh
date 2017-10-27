#!/bin/bash
ID=`date +%s`
export BROKER_HOST=127.0.0.1
export BROKER_PORT=5672
celery -n ${ID} -A broccoli.celery_app worker --loglevel=debug
