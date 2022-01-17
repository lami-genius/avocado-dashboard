from gevent.pywsgi import WSGIServer
from app import flask_server as application

http_server = WSGIServer(('', 5000), application)
http_server.serve_forever()
