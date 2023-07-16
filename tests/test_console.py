#!/usr/bin/python3

"""
Module contains tests to check if files pass Pep8 guidelines
"""
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
        """ Test for EOF method """
        with patch('builtins.input', return_value='EOF'):
            self.assertTrue(self.cmd.do_EOF(''))
