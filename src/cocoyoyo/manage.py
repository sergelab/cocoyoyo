# coding: utf-8

from flask.ext.script import Server, Manager
from flask.ext.script.commands import Clean, ShowUrls

from .init import app


manager = Manager(app)
manager.add_command('clean', Clean())
manager.add_command('routes', ShowUrls())
manager.add_command('runserver', Server())


@manager.command
def fastcgi():
    """
    Run application as fastcgi
    """
    from flup.server.fcgi import WSGIServer

    class ScriptNameStripper(object):
        def __init__(self, app):
            self.app = app

        def __call__(self, environ, start_response):
            environ['SCRIPT_NAME'] = ''
            return self.app(environ, start_response)

    wapp = ScriptNameStripper(app)
    WSGIServer(wapp).run()


def main():
    manager.run()
