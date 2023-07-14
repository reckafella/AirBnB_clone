#!/usr/bin/python3

"""
Module contains tests to check if files pass Pep8 guidelines
"""
import pycodestyle
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
