#!/usr/bin/env python3
"""
Module: review.py

Review class, which represents a review.

Class:
    Review:
         review with attributes such as place ID, user ID, and text.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review with attributes such as place ID, user ID, and text.
    """
    place_id = ""
    user_id = ""
    text = ""
