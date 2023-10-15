#!/usr/bin/env python3
"""
The Amenity module - Amenity class for representing amenities.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity in the application """

    name = ""
    """str: Name of the amenity."""
