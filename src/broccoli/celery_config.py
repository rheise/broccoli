import os

BROKER_URL = (
    'pyamqp://broccoli:secret@%s:%s/broccoli'
    % (
        os.environ.get('BROKER_HOST', 'rabbitmq'),
        os.environ.get('BROKER_PORT', '5672')
    )
)
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_EVENT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://redis/0'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
