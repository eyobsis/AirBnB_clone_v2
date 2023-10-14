#!/usr/bin/python3
from datetime import datetime
import uuid


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
            self.created_at = self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        Converts the instance to a dictionary for serialization.

        Returns:
            dict: A dictionary representation of the instance's attributes.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
