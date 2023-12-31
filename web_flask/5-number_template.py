#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

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
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text="is cool"):
    """Route that displays 'Python' followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    """Route that displays 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Route that displays a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
