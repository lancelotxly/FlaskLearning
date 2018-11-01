'''
Basic construction of Flask Web app
'''
'''
1. Initialization: create a object of Flask  # Web Client <--Request/Response(# WSGI)-->Web Server(# Flask app)
                   app = Flask(__name__)   # almost __name__, Flask determines the root dir to find the source file through '__name__' 
'''
from flask import Flask, request, redirect, abort, make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

'''
2. Route and view function:  # route includes url and method
                             @app.route('/url', methods=['GET', 'POST'])  # GET: only request source;   POST: post user form and request source
                             # view-function returns corresponding responses, which includes Body, Status Code(default=200 successful), header(dict)
                               def func():
                                   #...
                                   return Body, Status Code, Header
                            
                             can also use: 
                                 response = make_response(Body, Status Code, Header)  
                                 return  response
                                 
                             Status Code:  200 successfully; 302 redirect; 404 not found
'''
# normal
@app.route('/user/<name>', methods=['GET',])
def user(name):
    return '<h1>Hello, %s</h1>' % name

# request the information of Request send by Client
@app.route('/request',methods=['GET',])
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s</h1>' % user_agent

# redirect: just return a /url
@app.route('/',methods=['GET','POST'])
def home():
    return redirect('www.bilibili.com')

# abort 404
@app.route('/user',methods=['GET'])
def nofound():
    if not user:
        abort(404)
    return '<h1>Hello</h1>'

# make_response
@app.route('/Cindy',methods=['GET'])
def Cindy():
    body = '<h1>I love you</h1>'
    status = 302
    header = {'Content-Type':'text/html'}
    response = make_response(body, status, header)
    return response
'''
3. Start the flask server:   if __name__ == "__main__"  # makes sure only when this .py run, the server will be started
                                  app.run('host',port)       # can make some config to the server
                                                  
'''
if __name__ == "__main__":
    manager.run()  # default: 127.0.0.1:5000