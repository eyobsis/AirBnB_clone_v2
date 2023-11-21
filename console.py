#!/usr/bin/python3
"""Command interpreter module"""
import cmd
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance with given parameters"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        params = {}
        for param in args[1:]:
            param_parts = param.split("=")
            if len(param_parts) != 2:
                # Skip parameters that don't fit the required syntax
                continue
            key, value = param_parts
            value = value.replace("_", " ")  # Replace underscores with spaces in string values
            if value.startswith('"') and value.endswith('"'):
                # String value
                value = value[1:-1].replace('\\"', '"')  # Handle escaped double quotes
            elif "." in value:
                # Float value
                try:
                    value = float(value)
                except ValueError:
                    # Skip invalid float values
                    continue
            else:
                # Integer value
                try:
                    value = int(value)
                except ValueError:
                    # Skip invalid integer values
                    continue
            params[key] = value

        new_instance = models.classes[class_name](**params)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in storage.all():
            storage.all().pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if not args:
            instances = storage.all()
        elif args[0] in models.classes:
            instances = storage.all(models.classes[args[0]])
        else:
            print("** class doesn't exist **")
            return

        print("[", end="")
        print(", ".join(str(instance) for instance in instances.values()), end="")
        print("]")

    def precmd(self, line):
        """Preprocess the command line to handle <class name>.all(), <class name>.count(), <class name>.show(<id>), <class name>.destroy(<id>), and <class name>.update(<id>, <attribute dict>) syntax"""
        parts = line.split('.')
        if len(parts) == 2:
            class_name, method = parts
            if method == 'all()':
                return 'all ' + class_name
            elif method == 'count()':
                return 'count ' + class_name
            elif method.startswith('show(') and method.endswith(')'):
                obj_id = method[5:-1]
                return 'show ' + class_name + ' ' + obj_id
            elif method.startswith('destroy(') and method.endswith(')'):
                obj_id = method[8:-1]
                return 'destroy ' + class_name + ' ' + obj_id
            elif method.startswith('update(') and method.endswith(')'):
                update_args = method[7:-1]
                update_args_list = update_args.split(', ', 1)
                if len(update_args_list) == 2:
                    obj_id = update_args_list[0].strip('"')
                    attribute_dict_str = update_args_list[1].strip('{}')
                    return 'update ' + class_name + ' ' + obj_id + ' ' + attribute_dict_str
        return line

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instances = storage.all(models.classes[class_name])
        print(len(instances))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
