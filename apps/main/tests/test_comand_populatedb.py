"""
Module to test the command 
    `python3 manage.py populatedb`
"""
import unittest
from io import StringIO
from django.core.management import call_command
from django.test import TestCase

class PopulatedbTest(TestCase):

    def setUp(self):
        """
        Call populatedb command, and puts all
        the printed lines at 'out'.
        """
        self.out = StringIO()
        call_command('populatedb', stdout=self.out)

    @unittest.skip("It's not finished!")
    def test_command_output(self):
        """
        Tests the command output with assertIn and assertNotIn
        """
        self.assertIn("Text that should output when success", self.out)
        self.assertNotIn("FAILURE", self.out)


