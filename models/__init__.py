#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
"""__init__ magic method for models directory
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
