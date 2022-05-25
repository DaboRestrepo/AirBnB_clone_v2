#!/usr/bin/python3
"""Start a flask app."""
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(current):
    """Remove the current SQL session"""
    storage.close()


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states(id):
    """Display HTML state content."""
    if id:
        id = 'State.' + id
        states = storage.all(State)
    else:
        states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('9-states.html', id=id, states=states,
                           cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
