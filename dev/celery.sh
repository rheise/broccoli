#!/bin/bash
celery -A switchconnex.service_jobs.celery_app $@
