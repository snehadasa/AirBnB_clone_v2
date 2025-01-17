#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State, City
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_state():
    """render template 8-cities_by_states.html"""
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def app_teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
