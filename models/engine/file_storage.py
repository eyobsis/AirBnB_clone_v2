#!/usr/bin/env python3
"""
Defines the file storage class.
"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
import sys
sys.path.append("/AirBnB_clone/models/engine")

class FileStorage:

    """ Represents a file-based storage system for objects
    Attributes:
        __file_path (str): The path to the JSON file for storing serialized
        objects.
        __objects (dict): A dictionary that stores all the created objects.
        classes (dict): A dictionary mapping class names to their corresponding
        """
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "State": State,
        "City": City,
        "Review": Review,
    }

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or a dictionary of objects filtered
        by class.

        Args:
            cls (type, optional): The class to filter the objects. Defaults to
            None.

        Returns:
            dict: A dictionary of all objects or a dictionary of objects
            filtered by class.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for obj_id, obj in self.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[obj_id] = obj
            return filtered_objects

    def new(self, obj):
        """
        Sets the given object in __objects with key <obj class name>.id.

        Args:
            obj (object): The object to be set in __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = self.classes.get(class_name)
                    if cls is not None:
                        if class_name == "User":
                            obj = cls()
                            obj.__dict__.update(obj_dict)
                        else:
                            obj = cls(**obj_dict)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def count(self, cls=None):
        """
        Returns the number of objects in storage or the number of objects
        filtered by class.

        Args:
            cls (type, optional): The class to filter the objects. Defaults to
            None.

        Returns:
            int: The number of objects in storage or the number of objects
            filtered by class.
        """
        if cls is None:
            return len(self.__objects)
        else:
            count = 0
            for obj in self.__objects.values():
                if isinstance(obj, cls):
                    count += 1
            return count

    def serialize(self):
        """
        Serializes objects stored in the __objects attribute to a JSON file.
        """
        serialized_objects = {}
        for obj_id, obj in self.__objects.items():
            serialized_objects[obj_id] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file, indent=4)

    def deserialize(self):
        """
        Deserializes the JSON file to recreate the objects and store them in
        the __objects attribute.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                serialized_objects = json.load(file)
                for obj_id, obj_dict in serialized_objects.items():
                    class_name = obj_dict['__class__']
                    cls = self.classes.get(class_name)
                    if cls is not None:
                        if class_name == "User":
                            obj = cls()
                            obj.__dict__.update(obj_dict)
                        else:
                            obj = cls(**obj_dict)
                        self.__objects[obj_id] = obj
