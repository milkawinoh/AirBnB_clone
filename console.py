#!/usr/bin/python3
"""
    This module implements a command interpreter for the Holberton
    School AirBnB project. It allows the user to create, update,
    and delete instances, as well as retrieve
    information about existing instances.

"""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """
    This class implements a command-line interpreter for
    the Holberton School AirBnB project. It allows users
    to interact with the underlying data models and perform
      various actions such as creating, updating, and deleting instances.

    Attributes:
        classes (dict): A dictionary mapping class names to their
            corresponding Python class objects for the AirBnB project.

    Methods:
        do_EOF(self, line): Handles the end of the file input.
        precmd(self, line): Executes a command before parsing it.
        do_quit(self, arg): Exits the current session.
        emptyline(self): Defines the behavior when an empty
        line is entered.
        postloop(self): Performs actions after the loop ends.
        do_create(self, arg): Creates a new instance of a specified class.
        do_show(self, arg): Displays the string representation
        of an instance.
        do_destroy(self, arg): Deletes an instance based on
        the class name and ID.
        do_all(self, arg): Returns a list of all instances
        or a list of instances of a specified class.
        do_count(self, arg): Retrieves the number of
        instances of a specified class.
        do_update(self, arg): Updates an instance based
        on the class name and ID.
    """

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
        }

    prompt = '(hbnb) '

    def do_EOF(self, line):
        "Exit the program gracefully using EOF signal (Ctrl + D)"
        print()
        return True

    def precmd(self, line):
        """Performs functions before execution of commands."""
        line = line.replace("()", "").split(".")
        print(line)
        if len(line) != 1:
            line[0], line[1] = line[1], line[0]
            print(line)
            cmd = line[1]
            result = re.search(r'(\w+)\("([^"]*)"\)', line[0])
            if result:
                line[0] = result.group(1)
                line[1] = result.group(2)
            line.insert(1, cmd)
        line = " ".join(line)
        print(line)
        return line

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def emptyline(self):
        "pass when empty string is passed"
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name in self.classes:
            instance = self.classes[class_name]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)

        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Retrieve all instances of a specified class.
        Usage: <class name>.all()
        If no class name is provided, all instances
        from all classes are retrieved.
        If the specified class does not exist,
        an appropriate message is displayed.
        Prints the string representations of the retrieved instances.
        """
        list_instances = []
        if not arg:
            all_instances = storage.all()
            print(str(list_instances))
            return
        else:
            class_name = arg.split()[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            all_instances = storage.all()
            for key, value in all_instances.items():
                if class_name == value.__class__.__name__:
                    list_instances.append(str(value))
            print(list_instances)
        return

    def do_count(self, arg):
        """
        retrieve the number of instances
        of a class: <class name>.count().
        """
        all_instances = storage.all()
        count = 0
        arg = arg.split()
        class_name = arg[0]
        for key, value in all_instances.items():
            if class_name == value.__class__.__name__:
                count = count + 1
        print(count)
        return

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if len(args) < 2:
            print(len(args))
            print("** instance id missing **")
            return
        id = args[1]
        if len(args) < 3:
            print(len(args))
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print(len(args))
            print("** value missing **")
            return
        attribute_value = args[3]

        all_objects = storage.all()
        key = "{}.{}".format(class_name, id)
        if key not in all_objects:
            print("** no instance found **")
            return

        obj = all_objects[key]
        if attribute_name in obj.to_dict():
            if attribute_name not in ['id', 'created_at', 'updated_at']:
                setattr(obj, attribute_name, attribute_value)
                storage.save()
            else:
                return
        else:
            print("** attribute name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()