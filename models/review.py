#!/usr/bin/env python3
"""
Module: review.py

This module defines the Review class, which represents a review.

Class:
    Review:
         review with attributes such as place ID, user ID, and text.
"""
from base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review with attributes such as place ID, user ID, and text.
    """

    def __init__(self):
        """
        Bigins a new instance of Review class.

        Attributes:
            place_id (str): The ID of the place associated with the review.
                            It will be the Place.id.
            user_id (str): The ID of the user associated with the review.
                           It will be the User.id.
            text (str): The text content of the review.
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
