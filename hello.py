'''
Basic construction of Flask Web app
'''
'''
1. Initialization: create a object of Flask  # Web Client <--Request/Response-->Web Server <--WSGI--> Flask app
                   app = Flask(__name__)   # almost __name__, Flask determines the root dir to find the source file through '__name__' 
'''
from flask import Flask, request, redirect, abort

app = Flask(__name__)

'''
2. Route and view function:  # route includes url and method
                             @app.route('/url', methods=['GET', 'POST'])  # GET: only request source;   POST: post user form and request source
                             # view function returns corresponding responses, which includes Body, Status Code(default=200 successful), header(dict)
                               def func():
                                   #...
                                   return Body, Status Code, Header
                            
                             can also use: 
                                 response = make_response(Body, Status Code, Header)  
                                 return  response
                                 
                             Status Code:  200 successfully; 302 redirect; 404 not found
'''


@app.route('/user/<name>', methods=['GET',])
def user(name):
    return '<h1>Hello, %s</h1>' % name

# use request:  request from Client's request(header+body)
@app.route('/request',methods=['GET'])
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

# Status Code test: 302, 404
@app.route('/', methods=['GET','POST'])
def home():
    return redirect('http://www.bilibili.com')

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = id
    if not user:
        abort(404)
    return  '<h1>Hello, %s</h1>' % user

'''
3. Start the flask server:   if __name__ == "__main__"  # makes sure only when this .py run, the server will be started
                             app.run()       # can make some config to the server
'''
if __name__ == "__main__":
    app.run()