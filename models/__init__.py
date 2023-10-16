#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
"""
This module initiates a FileStorage instance and reloads it from a file
(if it exists).
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

""" Define the classes dictionary
"""

classes = {
    'BaseModel': BaseModel,
    'State': State,
    'City': City,
    'Place': Place,
    'Amenity': Amenity,
    'Review': Review,
}
class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

