#!/usr/bin/python3
""" command interface for air bnb project"""
import cmd
import sys
import re 
import models
from models.user import User
from models.engine import file_storage
import json
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """End of file(EOF)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
    pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance = models.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return

        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return

        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if not arg:
            instances = models.storage.all().values()
        else:
            class_name = arg
            if class_name not in models.classes:
                print("** class doesn't exist **")
                return
            instances = [v for k, v in models.storage.all().items()
                         if class_name in k]

        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** A class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in models.classes:
            print("** A class doesn't exist **")
            return

        if len(args) < 2:
            print("** A instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in models.storage.all():
            print("** A no instance found **")
            return

        if len(args) < 3:
            print("** A attribute name missing **")
            return

        if len(args) < 4:
            print("** A value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = models.storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
