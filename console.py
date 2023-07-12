#!/usr/bin/python3

"""
Module contains class implementing the console loop used by the Airbnb clone
"""

import cmd


class Console(cmd.Cmd):
    """
    class implementing entry point into Airbnb program

    attributes:
        prompt (str): prompt
    """
    prompt = "(hbnb)"

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
