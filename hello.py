from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/about")
def about():
    x=2+3
    return f"About me {x}"