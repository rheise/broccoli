from flask_apiblueprint import APIBlueprint


blueprint = APIBlueprint(__name__, __name__)


from . import test  # noqa
