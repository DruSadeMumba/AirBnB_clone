#!/usr/bin/python3
"""Importing the module for building commandline interface."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parsing_str(arg):
    """Extract a portion of the string."""
    curly_match = re.search(r"\{(.*?)}", arg)
    brackets_match = re.search(r"\[(.*?)]", arg)

    pattern_match = brackets_match if curly_match is None else curly_match

    if pattern_match is None:
        return [i.strip(",") for i in split(arg)]
    else:
        delim = split(arg[:pattern_match.span()[0]])
        return_list = [i.strip(",") for i in delim]
        return_list.append(pattern_match.group())
        return return_list


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
        input_arg = parsing_str(arg)
        arg_len = len(input_arg)

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
        input_arg = parsing_str(arg)
        arg_len = len(input_arg)

        if arg_len == 0:
            print("** class name missing **")
            return

        elif input_arg[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")

        elif arg_len == 1:
            obj = eval(input_arg[0])()
            obj.save()
            print(obj.id)

        else:
            return

    def do_all(self, arg):
        """Display all instances provided with classname or not."""
        input_arg = parsing_str(arg)
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
        input_arg = parsing_str(arg)
        arg_len = len(input_arg)

        if arg_len == 0:
            print("** class name missing **")

        elif input_arg[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")

        elif arg_len == 1:
            print("** instance id missing **")

        elif f"{input_arg[0]}.{input_arg[1]}" not in storage.all().keys():
            print("** no instance found **")

        else:
            del storage.all()[f"{input_arg[0]}.{input_arg[1]}"]
            storage.save()

    def do_update(self, arg):
        """Update the class attribute and save it."""
        input_arg = parsing_str(arg)
        arg_len = len(input_arg)

        if arg_len == 0:
            print("** class name missing **")
            return False

        if input_arg[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")
            return False

        if arg_len == 1:
            print('** instance id missing **')
            return False

        if arg_len == 2:
            print("** attribute name missing **")
            return False

        if f"{input_arg[0]}.{input_arg[1]}" not in storage.all():
            print("** no instance found **")
            return False

        if arg_len == 3 and not isinstance(eval(input_arg[2]), dict):
            print("** value missing **")
            return False

        if arg_len == 4:
            obj = storage.all()[f"{input_arg[0]}.{input_arg[1]}"]
            if input_arg[2] in obj.__class__.__dict__:
                obj.__dict__[input_arg[2]] =\
                    type(obj.__class__.__dict__[input_arg[2]])(input_arg[3])
            else:
                obj.__dict__[input_arg[2]] = input_arg[3]
        elif type(eval(input_arg[2])) == dict:
            obj = storage.all()[f"{input_arg[0]}.{input_arg[1]}"]
            for key, val in eval(input_arg[2]).items():
                if key in obj.__class__.__dict__ \
                        and type(obj.__class__.__dict__[key]) in {str, int, float}:
                    obj.__dict__[key] = type(obj.__class__.__dict__[key])(val)
                else:
                    obj.__dict__[key] = val
        storage.save()

    def do_count(self, arg):
        """Count No of instance of a class."""
        input_arg = parsing_str(arg)
        arg_len = len(input_arg)

        num = 0
        if arg_len == 0:
            print("** class name missing **")
        elif input_arg[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")
        else:
            for ist in storage.all().values():
                if input_arg[0] == ist.__class__.__name__:
                    num += 1
            print(num)

    def default(self, arg):
        """Handle function based on predefined keyword actions"""
        command_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        if "." in arg:
            split_arg = arg.split(".", 1)
            if "(" in split_arg[1] and ")" in split_arg[1]:
                command, rest = split_arg[1].split("(", 1)
                arguments = rest.rsplit(")", 1)[0]
                if command in command_dict.keys():
                    call = "{} {}".format(split_arg[0], arguments)
                    return command_dict[command](call)

        print("*** Not found: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
