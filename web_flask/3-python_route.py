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


@app.route('/c/<text>')
def C_text(text):
    """display “C ” followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python')
def Python_text(text="is cool"):
    """display “Python ” followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run()
