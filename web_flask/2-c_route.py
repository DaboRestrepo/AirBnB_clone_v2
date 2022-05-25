#!/usr/bin/python3
"""Start a Flask web app."""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Say hello to Holberton."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display the word HBNB."""
    return 'HBNB'


@app.route('/c/<text>')
def text(text):
    """Display a C following by the text variable."""
    if text.find('_'):
        text.replace('_', ' ')
    return 'C %s' % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
