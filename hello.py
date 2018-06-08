from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/lae")
def lae():
    return "Welcome to My World"
