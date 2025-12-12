from flask import Flask

app = Flask(__name__, static_folder="static")

# import dei blueprint
from app.routes.api import api
from app.routes.pages import pages

# registrazione dei blueprint
app.register_blueprint(api)
app.register_blueprint(pages)
