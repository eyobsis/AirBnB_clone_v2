#!/usr/bin/env python3
"""
Module: place.py

Which defines the Place class, which represents a place or location.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class is  a place with various attributes such as city ID, user ID,
    name, description, number of rooms, number of bathrooms, maximum guests,
    price per night, latitude, longitude, and a list of amenity IDs.
    """

    def __init__(self):
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
