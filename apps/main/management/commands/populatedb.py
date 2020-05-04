from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.main.models import *

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database for testing locally purposes'

    def handle(self, *args, **options):
        self._create_users()
        self._create_bands()
        self._create_establishment()
        self._create_events()

    def _create_users(self):
        """
        Creates all users for testing
        """
        self.users = []
        userparms = [('user1', 'testpass123'),
                ('user2', 'testpass123'),
                ('user3', 'testpass123'),
                ('user4', 'testpass123')]
        for us, ps in userparms:
            self.users.append(
                User.objects.create_user(username=us, password=ps)
                )

    def _create_bands(self):
        """
        Creates all bands
        """
        pass

    def _create_establishment(self):
        """
        Creates all the establishments.
        """
        self.establishments = [
            Establishment(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=self.users[0]), 
            Establishment(name="Bar Pac2", address="C/Major n9", email="paco96@gmail.com", mobile="100000000", user=self.users[1]),
            Establishment(name="Bar Pac3", address="C/Major n9", email="paco96@gmail.com", mobile="200000000", user=self.users[2]),
            Establishment(name="Bar Pac4", address="C/Major n9", email="paco96@gmail.com", mobile="300000000", user=self.users[3]),
        ]
        for est in self.establishments:
            est.save()


        

    def _create_events(self):
        """
        Creates all the events needed.
        """
        pass

