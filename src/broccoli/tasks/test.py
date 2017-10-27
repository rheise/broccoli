from broccoli.celery_app import app
import time


@app.task(bind=True)
def test(self):
    count = 100
    for i in range(count):
        time.sleep(1)
        self.update_state(
            state='PROGRESS',
            meta={'current': i, 'total': count}
        )
    return 'RESULT'
