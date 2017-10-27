from . import job


def init_app(app):
    app.register_blueprint(job.blueprint, url_prefix='/job')
