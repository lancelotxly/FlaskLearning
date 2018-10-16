'''
Web app: development process, HTTP, WSGI
'''

'''
development process: 1. Static Web page. 
                           Server can't get the information of Client, no interaction between Client and Server
                     2. CGI(Common Gateway Interface)
                           Client can hand up form through CGI protocol
                     3. ASP/JSP/PHP
                           Server can insert script into .html file, and generate corresponding .html file according to Client information
                     4. MVC(Model-View-Controller)
                           To avoid the problem that inserted script will lead poor maintenance. 
'''

'''
HTTP: Based on TCP/IP, server in application layer.
      HTTP flow: 
                1. Browser-->Http Request--> Server
                2. Server generates corresponding Http Response
                3. Server-->Http Response--> Client
                tips: a Http Request could deal with only one resource: HTML, image, video
      
      HTTP Request: 
                   1. GET (request resources only)
                      Request Header:
                                     GET /url HTTP/1.1      # url, e.g www.sina.com/url
                                     Host: www.sina.com     # the domain name
                                     key: value             # parameters
                                 
                   2. POST(post information of user and request resources)
                      Reques Header:
                      Body:
                      
      HTTP Response:
                   Response Header:
                                  HTTP/1.1 Response code   # 200(success), 3xx(redirect), 4xx(errors in Client request), 5xx(errors in Server)
                                  Content-Type: text/html  # e. g
                   Body:
                        html, image, video 
'''

'''
WSGI(Web Server Gateway Interface): Receive Http request, analysis request, Send Http response
                 
                 1. define application function
                  e. g.   def application(environ, start_response):
                             path = environ['PATH_INFO']
                             start_response('200 0k',[('Content-Type','text/html')])
                             body = '<h1>Hello %s</h1>' % (path[1:] or 'web')
                             return [body.encode('utf-8')]
                             
                 2. define server
                 e. g.   from wsgiref.simple_server import make_server
                         httpd = make_server('host', port, application)
                         httpd.server_forever() 
'''
def application(environ,start_response):
    path = environ['PATH_INFO']
    start_response('200 0k',[('Content-Type','text/html')])
    body = '<h1>Hello, %s</h1>' % (path[1:] or 'web')
    return [body.encode('utf-8')]