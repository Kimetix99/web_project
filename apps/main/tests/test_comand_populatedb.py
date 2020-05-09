"""
Module to test the command 
    `python3 manage.py populatedb`
"""
import unittest
from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from apps.main.models import Event, Band, Establishment
from django.contrib.auth import get_user_model

User = get_user_model()

class PopulatedbTest(TestCase):

    def setUp(self):
        """
        Call populatedb command, and puts all
        the printed lines at 'out'.
        """
        self.out = StringIO()
        call_command('populatedb', stdout=self.out)


    def test_command_output(self):
        """
        Tests the command output with assertIn and assertNotIn
        """
        self.assertEqual(len(User.objects.all()), 8)
        self.assertEqual(len(Band.objects.all()), 4)
        self.assertEqual(len(Establishment.objects.all()), 4)
        self.assertEqual(len(Event.objects.all()), 4)

