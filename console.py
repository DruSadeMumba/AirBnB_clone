#!/usr/bin/python3
"""Importing the module for building commandline interface."""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.engine.custom_exceptions import *
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parsing_str(input: str):
    """Extract a portion of the string."""
    arg = split(input)
    arg_length = len(arg)
    return arg, arg_length


class HBNBCommand(cmd.Cmd):
    """
    Building Commandline Interpreter.
    Attributes:
        intro (str): Tips for using Console interpreter
        prompt (str): User interactive tiext display.
    """
    __cls_list = storage.cls_list

    prompt = '(hbnb)> '

    def emptyline(self):
        """Displaying a prompt even when empty line."""
        pass

    def do_EOF(self, arg):
        """Exiting the console when reach EOF."""
        print()
        return True

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def do_show(self, arg):
        """Display the string representation of an instance
        grounding on the class name && id.
        """

        input_arg, arg_len = parsing_str(arg)

        if arg_len == 0:
            print("** class name missing **")

        elif input_arg[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")

        elif arg_len > 1:
            k = input_arg[0] + '.' + input_arg[1]
            if k in storage.all():
                dic = storage.all()
                print(dic[k])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_create(self, arg):
        """Creating a new instance of BaseModel,save it, and print the id."""

        input_arg, arg_len = parsing_str(arg)
        if arg_len == 0:
            print("** class name missing **")
            return

        elif arg_len == 1:
            obj = eval(input_arg[0])()
            obj.save()
            print(obj.id)

        else:
            return

    def do_all(self, arg):
        """Display all instances provided with classname or not."""

        input_arg = arg.split()
        arg_len = len(input_arg)
        if arg_len == 0:
            print([str(val) for val in storage.all().values()])

        elif input_arg[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")

        else:
            print([str(val) for key, val in storage.all().items()
                   if input_arg[0] in key])

    def do_destroy(self, arg):
        """Delete the instances of the class name, using ID and save it."""

        input_arg, arg_len = parsing_str(arg)
        if arg_len == 0:
            print("** class name missing **")

        elif arg_len > 1:
            try:
                storage.pop_classname_id(input_arg[0], input_arg[1])

            except InstanceIdNotFoundError:
                print("** no instance found **")

            except ClassNameNotFoundError:
                print("** class doesn't exist **")
        else:
            return

    def do_update(self, arg):
        """Update the class attribute and save it."""

        input_arg = arg.split()
        arg_len = len(input_arg)
        if arg_len == 0:
            print("** class name missing **")

        elif input_arg[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")

        elif arg_len == 1:
            print('** instance id missing **')

        else:
            k = input_arg[0] + '.' + input_arg[1]
            if k in storage.all():
                if arg_len > 2:
                    if arg_len == 3:
                        print("** value missing **")
                    else:
                        setattr(storage.all()[k],
                                input_arg[2],
                                input_arg[3][1:-1])
                        storage.all()[k].save()
                else:
                    print("** attribute name missing ** ")
            else:
                print("** no instance found ** ")

    def execute_method(self, arg):
        """Execute different class methods."""

        class_methods = ["all", "show", "count", "create"]
        try:
            for method in class_methods:
                if method in arg:
                    exec(f'print({arg})')
                    return
        except AttributeError:
            print("** attribute not found **")
        except InstanceIdNotFoundError:
            print("** no instance found **")
        except TypeError as e:
            attr = str(e).split()[-1].replace("_", " ")
            print("** {} missing **".format(attr))
        except Exception:
            print("** use correct syntax **")

    def default(self, arg):
        """Provide implementation for method found in class."""
        if '.' in arg and arg.endswith(')'):
            class_name = arg.split('.')[0]
            if class_name not in HBNBCommand.__cls_list:
                print("** class doesn't exist **")
                return
            return self.execute_method(arg)

        return super().default(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
