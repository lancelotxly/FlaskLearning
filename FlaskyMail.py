import os

from flask import Flask

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'stmp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
print(app.config)
print(os.environ)