#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State, City
app = Flask(__name__)
app.url_map.strict_slashes = False


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
            states = None
    return render_template('9-states.html', states=states, s_key=s_key)


@app.teardown_appcontext
def app_teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
