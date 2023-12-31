#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
from flask import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Route that displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Route that displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """Route that displays 'C' followed by the value of the text variable"""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text="is cool"):
    """Route that displays 'Python' followed by the value of the text variable"""
    return 'Python {}'.format(escape(text.replace('_', ' ')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
