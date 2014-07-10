import importlib

from flask import Flask, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/base.cfg')
    app.config.from_envvar('FLASK_SETTINGS')

    db.init_app(app)

    return app


def register_blueprints(app):
    rv = []

    if not app.config['BLUEPRINTS']:
        app.config['BLUEPRINTS'] = []

    for name in app.config['BLUEPRINTS']:
        m = importlib.import_module(name + '.views')
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
                app.logger.debug('Blueprint "{0}" registered'.format(name))
                rv.append(item)

    return rv


app = create_app()

with app.app_context():
    register_blueprints(app)

import models
import views
