#!/usr/bin/env python3
"""
Module: state.py

defines z State class, which represents a state.

"""
from base_model import BaseModel


class State(BaseModel):
    """
    Represents a state with attributes such as name.
    """
    name = ""

    def __init__(self):
        """
        Initializes a new instance of the State class.

        Attributes:
            name (str): The name of the state.
        """
        self.name = ""
