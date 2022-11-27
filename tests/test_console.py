#!/usr/bin/python3
"""
Test suite for console
"""
import sys
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO

class TestConsole(unittest.TestCase):
    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual('Prints the string representation of an \
                    instance based on the class name and id.\n', f.getvalue())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help create")
                self.assertEqual('Creates a new instance of a given \
                        class, saves it (to the JSON file) and prints the id.\n', f.getvalue())

                def test_create(self):
                    with patch('sys.stdout', new=StringIO()) as f:
                        HBNBCommand().onecmd("create BaseModel")
                        self.assertIsInstance(f.getvalue(), str)
                        with patch('sys.stdout', new=StringIO()) as f:
                        HBNBCommand().onecmd("create")
                        self.assertEqual(f.getvalue(), '** class name missing **\n')
                        with patch('sys.stdout', new=StringIO()) as f:
                            HBNBCommand().onecmd("create MyModel")
                            self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
                            def test_show(self):
                                with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("show")
                                    self.assertEqual(f.getvalue(), '** class name missing **\n')
                                    with patch('sys.stdout', new=StringIO()) as f:
                                    HBNBCommand().onecmd("show MyModel")
                                    self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
                                    with patch('sys.stdout', new=StringIO()) as f:
                                        HBNBCommand().onecmd("show BaseModel")
                                        self.assertEqual(f.getvalue(), '** instance id missing **\n')
                                        with patch('sys.stdout', new=StringIO()) as f:
                                            HBNBCommand().onecmd("show BaseModel 1111")
                                            self.assertEqual(f.getvalue(), '** no instance found **\n')

                                            def test_destroy(self):
                                                with patch('sys.stdout', new=StringIO()) as f:
                                                    HBNBCommand().onecmd("destroy")
                                                    self.assertEqual(f.getvalue(), '** class name missing **\n')
                                                    with patch('sys.stdout', new=StringIO()) as f:
                                                    HBNBCommand().onecmd("destroy MyModel")
                                                    self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
                                                    with patch('sys.stdout', new=StringIO()) as f:
                                                        HBNBCommand().onecmd("destroy BaseModel")
                                                        self.assertEqual(f.getvalue(), '** instance id missing **\n')
                                                        with patch('sys.stdout', new=StringIO()) as f:
                                                            HBNBCommand().onecmd("destroy BaseModel 1111")
                                                            self.assertEqual(f.getvalue(), '** no instance found **\n')

                                                            def test_all(self):
                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                    HBNBCommand().onecmd("all")
                                                                    self.assertIsInstance(f.getvalue(), str)
                                                                    with patch('sys.stdout', new=StringIO()) as f:
                                                                    HBNBCommand().onecmd("all BaseModel")
                                                                    self.assertIsInstance(f.getvalue(), str)
                                                                    with patch('sys.stdout', new=StringIO()) as f:
                                                                        HBNBCommand().onecmd("all MyModel")
                                                                        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')

                                                                        def test_update(self):
                                                                            with patch('sys.stdout', new=StringIO()) as f:
                                                                                HBNBCommand().onecmd("update")
                                                                                self.assertEqual(f.getvalue(), '** class name missing **\n')
                                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                                HBNBCommand().onecmd("update MyModel")
                                                                                self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
                                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                                    HBNBCommand().onecmd("update BaseModel")
                                                                                    self.assertEqual(f.getvalue(), '** instance id missing **\n')
                                                                                    with patch('sys.stdout', new=StringIO()) as f:
                                                                                        HBNBCommand().onecmd("update BaseModel 1111")
                                                                                        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
                                                                                        with patch('sys.stdout', new=StringIO()) as f:
                                                                                            HBNBCommand().onecmd("create BaseModel")
                                                                                            model_id = f.getvalue()
                                                                                            with patch('sys.stdout', new=StringIO()) as f:
                                                                                                HBNBCommand().onecmd(f"update BaseModel {model_id}")
                                                                                                self.assertEqual(f.getvalue(), '** attribute name missing **\n')
                                                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                                                    HBNBCommand().onecmd(f"update BaseModel {model_id} first")
                                                                                                    self.assertEqual(f.getvalue(), '** value missing **\n')
                                                                                                    def test_quit(self):
                                                                                                        with patch('sys.stdout', new=StringIO()) as f:
                                                                                                            HBNBCommand().onecmd("quit")
                                                                                                            self.assertEqual(f.getvalue(), '')
                                                                                                            def test_EOF(self):
                                                                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                    HBNBCommand().onecmd("EOF")
                                                                                                                    self.assertEqual(f.getvalue(), '\n')
                                                                                                                    def test_emptyline(self):
                                                                                                                        with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                            HBNBCommand().onecmd("")
                                                                                                                            self.assertEqual(f.getvalue(), '')
                                                                                                                            def test_basedotall(self):
                                                                                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                    HBNBCommand().onecmd("BaseModel.all()")
                                                                                                                                    self.assertNotIn('[City]', f.getvalue())
                                                                                                                                    self.assertNotIn('[Review]', f.getvalue())
                                                                                                                                    self.assertNotIn('[Place]', f.getvalue())
                                                                                                                                    self.assertNotIn('[Amenity]', f.getvalue())
                                                                                                                                    self.assertNotIn('[State]', f.getvalue())
                                                                                                                                    with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                        HBNBCommand().onecmd("BaseModel.all")
                                                                                                                                        self.assertIn('**', f.getvalue())
                                                                                                                                        def test_reviewdotall(self):
                                                                                                                                            with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                HBNBCommand().onecmd("Review.all()")
                                                                                                                                                self.assertNotIn('[BaseModel]', f.getvalue())
                                                                                                                                                self.assertNotIn('[User]', f.getvalue())
                                                                                                                                                self.assertNotIn('[State]', f.getvalue())
                                                                                                                                                self.assertNotIn('[Place]', f.getvalue())
                                                                                                                                                self.assertNotIn('[City]', f.getvalue())
                                                                                                                                                self.assertNotIn('[Amenity]', f.getvalue())
                                                                                                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                    HBNBCommand().onecmd("Review.all")
                                                                                                                                                    self.assertIn('**', f.getvalue())
                                                                                                                                                    def test_userdotall(self):
                                                                                                                                                        with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                            HBNBCommand().onecmd("User.all()")
                                                                                                                                                            self.assertNotIn('[BaseModel]', f.getvalue())
                                                                                                                                                            self.assertNotIn('[City]', f.getvalue())
                                                                                                                                                            self.assertNotIn('[Review]', f.getvalue())
                                                                                                                                                            self.assertNotIn('[Place]', f.getvalue())
                                                                                                                                                            self.assertNotIn('[Amenity]', f.getvalue())
                                                                                                                                                            self.assertNotIn('[State]', f.getvalue())
                                                                                                                                                            with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                                HBNBCommand().onecmd("User.all")
                                                                                                                                                                self.assertIn('**', f.getvalue())
                                                                                                                                                                def test_statedotall(self):
                                                                                                                                                                    with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                                        HBNBCommand().onecmd("State.all()")
                                                                                                                                                                        self.assertNotIn('[BaseModel]', f.getvalue())
                                                                                                                                                                        self.assertNotIn('[City]', f.getvalue())
                                                                                                                                                                        self.assertNotIn('[Review]', f.getvalue())
                                                                                                                                                                        self.assertNotIn('[Place]', f.getvalue())
                                                                                                                                                                        self.assertNotIn('[Amenity]', f.getvalue())
                                                                                                                                                                        self.assertNotIn('[User]', f.getvalue())
                                                                                                                                                                        with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                                            HBNBCommand().onecmd("State.all")
                                                                                                                                                                            self.assertIn('***', f.getvalue())
                                                                                                                                                                            def test_placedotall(self):
                                                                                                                                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                                                    HBNBCommand().onecmd("Place.all()")
                                                                                                                                                                                    self.assertNotIn('[BaseModel]', f.getvalue())
                                                                                                                                                                                    self.assertNotIn('[City]', f.getvalue())
                                                                                                                                                                                    self.assertNotIn('[Review]', f.getvalue())
                                                                                                                                                                                    self.assertNotIn('[State]', f.getvalue())
                                                                                                                                                                                    self.assertNotIn('[Amenity]', f.getvalue())
                                                                                                                                                                                    self.assertNotIn('[User]', f.getvalue())
                                                                                                                                                                                    with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                                                        HBNBCommand().onecmd("Place.all")
                                                                                                                                                                                        self.assertIn('**', f.getvalue())
                                                                                                                                                                                        def test_amenitydotall(self):
                                                                                                                                                                                            with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                                                                HBNBCommand().onecmd("Amenity.all()")
                                                                                                                                                                                                self.assertNotIn('[BaseModel]', f.getvalue())
                                                                                                                                                                                                self.assertNotIn('[City]', f.getvalue())
                                                                                                                                                                                                self.assertNotIn('[Review]', f.getvalue())
                                                                                                                                                                                                self.assertNotIn('[Place]', f.getvalue())
                                                                                                                                                                                                self.assertNotIn('[State]', f.getvalue())
                                                                                                                                                                                                self.assertNotIn('[User]', f.getvalue())
                                                                                                                                                                                                with patch('sys.stdout', new=StringIO()) as f:
                                                                                                                                                                                                    HBNBCommand().onecmd("Amenity.all")
                                                                                                                                                                                                    self.assertIn('**', f.getvalue())

