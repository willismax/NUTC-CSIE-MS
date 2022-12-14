from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"<h1>Hello, {escape(name)}!</h1>"

if __name__ == '__main__':
    app.run(port=8000, debug=True)



