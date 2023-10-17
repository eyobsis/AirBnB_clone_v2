#!/usr/bin/env python3
"""
Module: place module

Which defines the Place class, which represents a place or location.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    class with various attributes such as city ID, user ID,
    name, description, number of rooms, number of bathrooms, maximum guests,
    price per night, latitude, longitude, and a list of amenity IDs.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
