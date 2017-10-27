from celery import Celery

app = Celery(
    __name__,
    config_source='broccoli.celery_config'
)

import broccoli.tasks  # noqa
