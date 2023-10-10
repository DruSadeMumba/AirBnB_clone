#!/usr/bin/python3
"""Importing the module for building commandline interface."""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Building Commandline Interpreter.
    Attributes:
        intro (str): Tips for using Console interpreter
        prompt (str): User interactive tiext display.
    """
    intro = ("Welcome to AirBnB Console!, "
             "Use \"help\" to list available commands."
             )

    prompt = '(hbnb)> '

    def emptyline(self):
        """Displaying a prompt even when empty line."""
        pass

    def do_EOF(self, arg):
        pass

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def do_show(self, arg):
        pass

    def do_create(self, arg):
        pass

    def do_destroy(self, arg):
        pass

    def do_update(self, arg):
        pass


if __name__ == '__main__':
    if sys.stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        for input_line in sys.stdin:
            input_line = input_line.strip()
            if input_line:
                HBNBCommand().onecmd(input_line)
