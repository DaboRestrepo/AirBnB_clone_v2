#!/usr/bin/python3
"""Start a flask app."""
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states():
    """Display HTML state content."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(current):
    """Remove the current SQL session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
