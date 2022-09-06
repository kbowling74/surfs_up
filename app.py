# import flask dependency
from flask import Flask

# create Flask app instance
app = Flask(__name__)

# create flask route
@app.route('/')
def hello_world():
    return 'Hello World'
