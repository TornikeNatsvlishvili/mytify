from app.api import api_bp
from app.extensions import mongo, jwt_manager
from app.settings import ProdConfig

from flask import Flask


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(api_bp)


def register_extensions(app):
    mongo.init_app(app)
    jwt_manager.init_app(app)
