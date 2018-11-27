# from wsgiref.simple_server import make_server
# from SimpleWeb import application
#
# httpd = make_server('127.0.0.1',8000,application)
# httpd.serve_forever()

from wsgiref.simple_server import make_server
from SimpleWeb import application

httpd = make_server('127.0.0.1',8000,application)
httpd.serve_forever()