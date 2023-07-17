from io import StringIO
from unittest.mock import patch
import unittest

class TestConsole(unittest.TestCase):
    def test_console(self):
        """Test the functionality of the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            expected_output = "Prints the string representation of an instance\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_quit(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            expected_output = "Exits the program with formatting\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_EOF(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            expected_output = "Exits the program without formatting\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyClass")
            expected_output = "<instance_id>\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_show(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyClass <instance_id>")
            expected_output = "<instance_info>\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_destroy(self):
        """Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyClass <instance_id>")
            expected_output = "** no instance found **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyClass")
            expected_output = "[]\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_count(self):
        """Test the count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count MyClass")
            expected_output = "0\n"
            self.assertEqual(f.getvalue(), expected_output)
         
def test_do_update(self):
        """Test the do_update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Test updating an existing object
            HBNBCommand().onecmd("do_update MyClass <instance_id> attName attVal")
            expected_output = ""  # Adjust this based on your expectations
            self.assertEqual(f.getvalue(), expected_output)

            # Test updating a non-existing object
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("do_update MyClass non_existing_id attName attVal")
                expected_output = "** no instance found **\n"
                self.assertEqual(f.getvalue(), expected_output)

            # Test updating with missing attribute name
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("do_update MyClass <instance_id> ")
                expected_output = "** attribute name missing **\n"
                self.assertEqual(f.getvalue(), expected_output)

            # Test updating with missing attribute value
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("do_update MyClass <instance_id> attName")
                expected_output = "** value missing **\n"
                self.assertEqual(f.getvalue(), expected_output)
:
        
if __name__ == '__main__':
    unittest.main()
