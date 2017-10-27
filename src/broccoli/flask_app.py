import flask
from . import blueprints


def create_app():
    app = flask.Flask(__name__)
    blueprints.init_app(app)
    return app
