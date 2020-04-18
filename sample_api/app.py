from flask import Flask, Blueprint
from flask_cors import CORS
from .api import api
from .api.hello_world import ns as hello_world_ns

from healthcheck import HealthCheck, EnvironmentDump


def create_app():
    app = Flask(__name__)

    health = HealthCheck()
    envdump = EnvironmentDump()

    CORS(app)

    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    api.add_namespace(hello_world_ns, '/hello-world')
    app.register_blueprint(blueprint)
    app.add_url_rule("/health-check", "healthcheck", view_func=lambda: health.run())
    app.add_url_rule("/environment", "environment", view_func=lambda: envdump.run())

    return app
