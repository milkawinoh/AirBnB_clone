#!/usr/bin/python3
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

"""
    This module implements a command interpreter for the Holberton
    School AirBnB project. It allows the user to create, update,
    and delete instances, as well as retrieve
    information about existing instances.

"""


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

    prompt = '(hbnb)'

    def do_EOF(self, line):
        "exit"
        return True

    def precmd(self, line):
        """Performs functions before execution of commands
            arguments
        ;
        """
        line = line.replace("()", "").split(".")
        if len(line) != 1:
            line[0], line[1] = line[1], line[0]
            result = re.search(r'(\w+)\("([^"]*)"\)', line[0])
            if result:
                line[0] = result.group(1)
                line[1] = result.group(2)
                print(line)
            print(line)
        line = " ".join(line)
        print(line)
        return line

    def do_quit(self, arg):
        """quit out of the current session"""
        return True

    def emptyline(self):
        "pass when empty string is passed"
        pass

    def postloop(self):
        "print newline before exit off the session"
        print()

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
            basemodel_instance = BaseModel()
            basemodel_instance.save()
            print(basemodel_instance.id)
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
        print(key)
        if key in storage.all():
            print(key)
            print(storage.all()[key])
        else:
            print(key)
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
        """returns the dictionary __objects"""
        list_instances = []
        if not arg:
            all_instances = storage.all()
            if all_instances is not None:
                list_instances.append(str(all_instances))
                print(list_instances)
                return
            else:
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

    def do_count(self, arg):
        """
        retrieve the number of instances
        of a class: <class name>.count().
        """
        all_instances = storage.all()
        count = 0
        for key, value in all_instances.items():
            if arg == value.__class__.__name__:
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
            print("** instance id missing **")
            return
        id = args[1]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
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
