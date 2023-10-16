#!/usr/bin/env python3
"""
Module: state.py

defines z State class, which represents a state.

"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state with attributes such as name.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
