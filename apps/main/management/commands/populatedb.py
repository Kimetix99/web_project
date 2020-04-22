from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.main.models import *


class Command(BaseCommand):
    help = 'Populates the database for testing locally purposes'

    def handle(self, *args, **options):
        self._create_users()
        self._create_bands()
        self._create_establishment()

    def _create_users(self):
        """
        Creates all users for testing
        """
        pass

    def _create_bands(self):
        """
        Creates all bands
        """
        pass

    def _create_establishment(self):
        """
        Creates all the establishments.
        """
        pass

    def _create_events(self):
        """
        Creates all the events needed.
        """
        pass

