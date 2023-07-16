#!/usr/bin/python3

"""
Module contains tests to check if files pass Pep8 guidelines
"""
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import unittest
import os
import pep8


class TestPep8Guidelines(unittest.TestCase):
    """
    Class implements checks that all python files comply with pep8 guidelines
    """
    dot_py_files = []

    for (root, dirs, files) in os.walk('.', topdown=True):
        for file_ in files:
            if file_.endswith('.py'):
                file_path = os.path.join(root, file_)
                dot_py_files.append(file_path)

    def test_pep8_conformance(self):
        """
        Function tests whether all files comply with pep8 guidelines
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(self.dot_py_files)
        self.assertEqual(result.total_errors,
                         0, "Found code style errors (and warnings).")


class TestHBNBCommand(unittest.TestCase):
    """ Class used to test the console. """
    def setUp(self) -> None:
        """ Set up the console for each test """
        self.cmd = HBNBCommand()

    def tearDown(self) -> None:
        """ Clear everything from memory after each test """
        pass

    def test_do_EOF(self):
        """ Test for `EOF` method in 'do_EOF' method """
        with patch('builtins.input', return_value='EOF'):
            self.assertTrue(self.cmd.do_EOF(''))

    def test_do_help_EOF(self):
        """ Test for `help quit` """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.cmd.help_EOF()
            self.assertEqual(fake_output.getvalue(),
                             "Exits the program without formatting\n\n")

    def test_do_quit(self):
        """ Test for `quit` command in 'do_quit' method """
        self.assertTrue(self.cmd.do_quit(''))

    def test_do_help_quit(self):
        """ Test for `help quit` """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.cmd.help_quit()
            self.assertEqual(fake_output.getvalue(),
                             "Exits the program with formatting\n\n")

    def test_precmd(self):
        """ Test the return value of `precmd` method """
        # Invalid command
        line = 'some.command'
        result = self.cmd.precmd(line)
        self.assertEqual(result, line)

        # Invalid command
        line = 'User.show'
        result = self.cmd.precmd(line)
        self.assertEqual(result, line)

        # Valid command
        line = 'User.show("b0929058-a94f-4400-a743-c69e8afdea3f")'
        res = self.cmd.precmd(line)
        self.assertEqual(res, 'show User b0929058-a94f-4400-a743-c69e8afdea3f')

        # Valid command
        line = 'User.show()'
        res = self.cmd.precmd(line)
        self.assertEqual(res, 'show User')

    def test_do_create(self):
        """ Tests for `do create` method """
        # Case 1: no class name
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.cmd.do_create('')
            self.assertEqual(fake_output.getvalue(),
                             "** class name missing **\n")

        # Case 2: Non-existent class name
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.cmd.do_create('Person')
            self.assertEqual(fake_output.getvalue(),
                             "** class doesn't exist **\n")
