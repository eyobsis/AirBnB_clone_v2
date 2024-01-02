#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb')
def hbnb():
    """Displays a HTML page like 8-index.html"""
    states = sorted(list(storage.all(State).values()), key=lambda state: state.name)
    amenities = sorted(list(storage.all(Amenity).values()), key=lambda amenity: amenity.name)
    places = sorted(list(storage.all(Place).values()), key=lambda place: place.name)

    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
