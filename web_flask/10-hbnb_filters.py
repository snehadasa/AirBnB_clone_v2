#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State, City
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


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list')
def states_list():
    """render template 7-number.html"""
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states_id(id):
    """render template 9-states.html.html"""
    states = storage.all('State')
    s_key = None
    if id:
        s_key = "{}.{}".format('State', id)
        if s_key not in states:
            s_key = None
    return render_template('9-states.html', states=states, s_key=s_key, id=id)


@app.route('/hbnb_filters')
def hbnb_filters():
    return render_template('10-hbnb_filters.html',
                           states=storage.all('State').values(),
                           amenities=storage.all('Amenity').values())


@app.teardown_appcontext
def app_teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
