#!/usr/bin/env python3
"""
Module for the City class representing cities.
"""

from base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.

    Attributes:
        state_id (str):ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""  # it will be the State.id
    name = ""
