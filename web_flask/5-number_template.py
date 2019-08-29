#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def number_n(n):
    """display n if its an integer"""
    if type(n) == int:
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ display a HTML page only if n is an integer"""
    if type(n) == int:
        return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
