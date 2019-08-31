#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """print Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    """display HBNB!"""
    return "HBNB"


if __name__ == "__main__":
    app.run()
