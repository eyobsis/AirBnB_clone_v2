#!/usr/bin/python3
"""
Define the BaseModel class and returns json data
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    The `BaseModel` class represents a basic model with common attributes
    and methods used in the application.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes a new instance of `BaseModel`.

        __str__(self):
            Returns a string representation of the instance.

        save(self):
            Updates the `updated_at` attribute to the current date and time.

        to_dict(self):
            Converts the instance to a dictionary for serialization.

    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a formatted string representation of the instance.

        Returns:
            str: A string represent in the format "[Class] (ID) Attributes".
        """
        a = self.__class__.__name__
        b = self.id
        c = self.__dict__
        return "[{}] ({}) {}".format(a, b, c)

    def save(self):
        """
        Updates the `updated_at` attribute to the current date and time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts our instance to a dictionary for serialization.

        Returns:
            dict: A dictionary representation of instance's attributes.
        """
        the_data = self.__dict__.copy()
        the_data['__class__'] = self.__class__.__name__
        the_data['created_at'] = self.created_at.isoformat()
        the_data['updated_at'] = self.updated_at.isoformat()
        return the_data
