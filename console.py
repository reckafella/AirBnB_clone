#!/usr/bin/python3

"""
Module contains HBNBCommand Class. Class implements command line interpreter
for the project.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class implementing entry point into Airbnb program

    attributes:
        prompt (str): prompt
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """
        Exit the loop when user presses 'Ctrl+D' or types 'EOF'
        """
        return True

    def do_quit(self, line):
        """
        Exit loop when user types 'quit' on command line interpreter
        """
        return True

    def postloop(self) -> None:
        print()

    def help_EOF(self):
        """ Help for EOF """
        print("Exit the loop when user presses 'Ctrl+D' or types 'EOF'")

    def help_quit(self):
        """ Help for quit command """
        print("Exit loop when user types 'quit' on command line interpreter")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
