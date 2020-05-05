# import flask dependency
from flask import Flask

# create a new flask instance
app = Flask(__name__)

# define the root
@app.route("/")
def hello_world():
    return "Hello world"