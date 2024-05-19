#!/usr/bin/python3
"""
This script defines the HBnB console, entry point 
of the command interpreter for the application.
"""

import cmd
import re
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Entry point for the program."""

    prompt = "(hbnb) "

    __classes = {'BaseModel', 'State', 'City', 'Amenity', 'Place', 'Review', 'User'}

    def precmd(self, line):
        """This method updates the interpreter to handle various tasks on class instances."""
        tasks = ['all', 'count', 'destroy', 'show', 'create', 'update']
        for task in tasks:
            if '.' in line and line.endswith(task + '()'):
                class_name = line.split('.')[0]
                return f"{task} {class_name}"

            pattern = re.compile(rf'^\s*([a-zA-Z_]\w*)\.{task}\((.*?)\)\s*$')
            match = pattern.match(line)
            if match:
                class_name = match.group(1)
                args = [arg.strip('"') for arg in re.findall(r'"[^"]+"|\{[^}]+\}', match.group(2))]
                if task in ['show', 'destroy', 'update']:
                    return f"{task} {class_name} {', '.join(args)}"
                else:
                    return f"{task} {class_name}"
        return line

    def emptyline(self):
        """Does nothing when an empty line is entered."""
        pass

    def do_create(self, args):
        """Creates a new instance of a given class."""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            class_list = {
                'BaseModel': BaseModel,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review,
                'User': User
            }
            curr_obj = class_list[args]()
            curr_obj.save()
            print(f"{curr_obj.id}")
            storage.save()

    def do_show(self, arg):
        """Shows the string representation of an instance based on class name and id."""
        args = arg.split()
        obj_dictionary = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj_dictionary:
            print("** no instance found **")
        else:
            print(obj_dictionary[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        obj_dictionary = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj_dictionary:
            print("** no instance found **")
        else:
            del obj_dictionary[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances, optionally filtered by class name."""
        signal = 1
        new_obj = [str(value) for value in storage.all().values()]
        if not arg:
            signal = 0
            print(new_obj)
        else:
            args = arg.split()
            if args[0] in HBNBCommand.__classes:
                signal = 0
                new_obj = storage.all()
                name = args[0]
                new_obj = [str(value) for key, value in new_obj.items() if name == value.__class__.__name__]
                print(new_obj)

        if signal:
            print("** class doesn't exist **")

    def do_count(self, line):
        """Counts the number of instances of a given class."""
        if not line:
            count = len(storage.all())
            print(count)
            return

        class_name = line.split()[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            counter = sum(1 for obj in storage.all().values() if class_name == obj.__class__.__name__)
            print(counter)

    def do_update(self, arg):
        """Updates an instance by modifying the attribute."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        else:
            dict_available = re.search(r"(?<=\{)([^\}]+)(?=\})", arg)
            new_obj = storage.all()
            signal = 0

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for key, value in new_obj.items():
                temp_arg = args[1].replace('"', '').replace(',', '')
                new_arg = f"{args[0]}.{temp_arg}"
                if new_arg == key:
                    signal = 1
                    if dict_available:
                        std_dict = dict_available.group()
                        restruct_dict = f'{{{std_dict}}}'
                        a_json_dict = restruct_dict.replace('\'', '"')
                        re_objdict = json.loads(a_json_dict)
                        for n_key, n_value in re_objdict.items():
                            if n_key and n_value:
                                setattr(value, n_key, n_value)
                                storage.all()[new_arg].save()
                        return
                    elif len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        val1 = args[3].replace('"', '')
                        val2 = val1.replace(',', '')
                        key = args[2].replace('"', '').replace(',', '')
                        setattr(value, key, val2)
                        storage.all()[new_arg].save()

            if signal != 1:
                print("** no instance found **")

    def do_quit(self, line):
        """Exits the program."""
        return True

    def do_EOF(self, line):
        """Exits the program on EOF."""
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
