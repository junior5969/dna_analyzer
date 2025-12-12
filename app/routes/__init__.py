from flask import Flask
from app.routes.api import api
from app.routes.pages import pages

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(pages)
    return app