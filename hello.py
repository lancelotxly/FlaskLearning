'''
Basic of Flask:        Server<-->WSGI(Web Server Gateway Interface)<-->Client
                          |             ^
                          |--Flask app--|
Flow:
     1. Initialize
        from flask import Flask
        app = Flask(__name__)    # where '__name__' is the root dir of the app, which helps to find the sources
     2. Build link between 'Route' and 'ViewFunction', and define 'ViewFunction',
            where 'Route' is the URL which includes 'URL' and 'methods=GET/POST', 'GET': only request for sources; 'POST': request for sources and post form of client.
            'ViewFunction' is a function which receives the information of client, and generates response (includes Body, Status Code, Header) which can be package by 'make_response'
             Tips: the url map can be obtained by 'app.url_map', which not only include the url we defined and also a 'staticroute', which is a url for staticfile(e.g. .jpg)
        @app.route('url',methods=['GET','POST'])
        def ViewFunction():
            body = html
            status_code = 200 (ok), 204 (no content), 206 (partial content)
                          301 (moved permanently), 302 (temporarily)
                          400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (page not found)
                          500 (internal server error), 503 (service unavailable)
            header = dict()  # see note book
            response = make_response(body, status_code, header) # from flask import make_response
            return response
     3. Start
        if __name__ == '__main__':
            app.run()

Context manage:  Flask use 'Context manage' to ensure some contexts globally in one thread, where for one user (or client) Flask will assign a thread
                 where the contexts include: 1) program context: current_app # the object of current app
                                                                 g # a interim object to reserve info.
                                             2) requirement context: request  # request object of HTTP Request
                                                                     session  # to reserve some important dict
                 where the flow of 'Context manage' is: 1) get the context of 'app'
                                                           app_ctx = app.app_context()
                                                        2) push the context
                                                           app_ctx.push()

hook function: some functions execute before of after ViewFunction
               before_first_request; before_request; after_request; teardown_request

Flask extension: All extension packages are managed in flask.ext
                 Flask-Script   # can plunge paras from order
'''
from flask import Flask, make_response, request, redirect, abort
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/', methods=['GET','POST'])
def home():
    body = '<h1>Welcome to my blog</h1>'
    status_code = 200
    header = {'Content-Type':'text.html'}
    response = make_response(body,status_code,header)
    return body

@app.route('/request',methods=['GET',])
def getInfo():
    user_agent = request.headers.get('User-Agent')   # from flask import request
    return '<h1>Your browser is %s</h1>' % user_agent

@app.route('/redirect',methods=['GET','POST'])
def redirectTo():
    return redirect('http://www.bilibili.com')  # from flask import redirect;  redirect('url')

@app.route('/user/<name>',methods=['GET',])
def user(name):
    if not user:
        abort(404)       # from flask import abort
    return '<h1>Hello, %s</h1>' % name

if __name__ == '__main__':
    manager.run()