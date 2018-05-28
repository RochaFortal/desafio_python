#coding: utf-8
import os
import sys
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from tornado.options import options, define, parse_command_line
import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.wsgi

ANGULARJS_APP = os.path.join(
    os.path.dirname(settings.BASE_DIR), 'client')
os.environ['DJANGO_SETTINGS_MODULE'] = 'startproject.settings'

STATIC_ROOT = settings.STATIC_ROOT

#define('num_process', type=int, default=2)
PORT = 8000
NUM_PROCESS = 2
define('port', type=int, default=PORT)

if settings.DEBUG:
    define('autoreload', settings.DEBUG, group='application')

def make_app():
    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)
    urls_to_tornado = [
        (r'/static/?(.*)', tornado.web.StaticFileHandler,
            {'path': STATIC_ROOT, 'default_filename': 'index.html'}),
        (r'/api/(.*)', tornado.web.FallbackHandler, dict(fallback=container)),
        (r'/?(.*)', tornado.web.StaticFileHandler,
            {'path': ANGULARJS_APP, 'default_filename': 'index.html'}),
    ]
    return tornado.web.Application(
        urls_to_tornado,
        **options.group_dict('application'))


class Command(BaseCommand):
    help = 'Iniciar o projeto django usando o e servindo com o tornado'

    def handle(self, *args, **kwargs):
        tornado.options.parse_command_line()
        tornado_app = make_app()
        server = tornado.httpserver.HTTPServer(tornado_app)
        if settings.DEBUG:
            server.listen(PORT)
        else:
            server.bind(PORT)
            server.start(NUM_PROCESS)
        sys.stdout.write(
            f'Starting development server at port: {PORT}\n')
        tornado.ioloop.IOLoop.instance().start()