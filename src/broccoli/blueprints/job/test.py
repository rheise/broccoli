from . import blueprint
from broccoli import tasks


@blueprint.route('/test', methods=['GET'])
def start_test():
    result = tasks.test.test.delay()
    return result.id, 202


@blueprint.route('/test/<job_id>/status', methods=['GET'])
def get_test_status(job_id):
    result = tasks.test.test.AsyncResult(job_id)
    return result.state, 200


@blueprint.route('/test/<job_id>/result', methods=['GET'])
def get_test_result(job_id):
    result = tasks.test.test.AsyncResult(job_id)
    print(result)
    if result.ready():
        print(result.get())
        return result.get(), 200
    return 'NOT READY', 202
