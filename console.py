class HBNBCommand(cmd.Cmd):
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

    def do_help(self, line):
        """
        Print help information
        """
        if line:
            # Print help for a specific command
            print(self.get_help(line))
        else:
            # Print general help
            print("Available commands:")
            for cmd in self.list_commands():
                print(cmd)
        return True

    def do_line(self, line):
        """
        Handle an empty line
        """
        if not line:
            return
        else:
            return cmd.Cmd.do_line(self, line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
