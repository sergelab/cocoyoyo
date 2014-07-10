from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/base.cfg')
    app.config.from_envvar('FLASK_SETTINGS')

    db.init_app(app)

    return app


app = create_app()

import models
import views
