import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class ConsoleTestCase(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
            self.assertIn("quit  help  create  show  destroy  update  all", output)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f2:
                self.console.onecmd("show BaseModel {}".format(obj_id))
                output = f2.getvalue().strip()
                self.assertIn(obj_id, output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f2:
                self.console.onecmd("destroy BaseModel {}".format(obj_id))
                output = f2.getvalue().strip()
                self.assertFalse(output)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f2:
                self.console.onecmd("update BaseModel {} name 'New Name'".format(obj_id))
                self.console.onecmd("show BaseModel {}".format(obj_id))
                output = f2.getvalue().strip()
                self.assertIn("'name': 'New Name'", output)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            with patch('sys.stdout', new=StringIO()) as f2:
                self.console.onecmd("all BaseModel")
                output = f2.getvalue().strip()
                self.assertIn("BaseModel", output)

if __name__ == '__main__':
    unittest.main()
