from broccoli.celery_app import app
import time


@app.task
def test():
    time.sleep(10)
    return 'OK'
