from django.utils import timezone
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
        user1 = User.objects.create_user(username="skewiff", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        user2 = User.objects.create_user(username="tessatioarina", password="testingpaco123", email="paco@gmail.co", first_name="Paco", last_name="Rodriguez")
        user3 = User.objects.create_user(username="drei-jazz", password="testingpaco123", email="paco@gmail.om", first_name="Paco", last_name="Rodriguez")
        user4 = User.objects.create_user(username="angelo-mikha", password="testingpaco123", email="paco@gmail.cm", first_name="Paco", last_name="Rodriguez")
        user5 = User.objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        user6 = User.objects.create_user(username="paquito1", password="testingpaco123", email="paco@gmail.co", first_name="Paco", last_name="Rodriguez")
        user7 = User.objects.create_user(username="paquito2", password="testingpaco123", email="paco@gmail.om", first_name="Paco", last_name="Rodriguez")
        user8 = User.objects.create_user(username="paquito3", password="testingpaco123", email="paco@gmail.cm", first_name="Paco", last_name="Rodriguez")
        self.users = [user1, user2, user3, user4, user5, user6, user7, user8]

    def _create_bands(self):
        """
        Creates all bands
        """
        band1 = Band.objects.create(name="itacaband", web_link='spotify:artist:5qPeAT4ikl6gJNUexAOEy0', playlist='https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0',      email="skeewiff@gmail.com", mobile="000000000", user=self.users[0])
        band2 = Band.objects.create(name="metallica", web_link='spotify:artist:5qPeAT4ikl6gJNUexAOEy0', playlist='https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0', email="tessatioarina@gmail.com", mobile="100000000", user=self.users[1])
        band3 = Band.objects.create(name="Maravillosa Orquesta del Alchol", web_link='spotify:artist:5qPeAT4ikl6gJNUexAOEy0', playlist='https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0',     email="tessatioarina@gmail.com", mobile="200000000", user=self.users[2])
        band4 = Band.objects.create(name="Oques Grasses", web_link='spotify:artist:5qPeAT4ikl6gJNUexAOEy0', playlist='https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0',  email="angelo@gmail.com", mobile="300000000", user=self.users[3])
        self.bands = [band1, band2, band3, band4]


    def _create_establishment(self):
        """
        Creates all the establishments.
        """
        est1 = Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=self.users[4])
        est2 = Establishment.objects.create(name="Bar Pac2", address="C/Major n9", email="paco96@gmail.com", mobile="100000000", user=self.users[5])
        est3 = Establishment.objects.create(name="Bar Pac3", address="C/Major n9", email="paco96@gmail.com", mobile="200000000", user=self.users[6])
        est4 = Establishment.objects.create(name="Bar Pac4", address="C/Major n9", email="paco96@gmail.com", mobile="300000000", user=self.users[7])
        self.est = [est1, est2, est3, est4]

        
        

    def _create_events(self):
        """
        Creates all the events needed.
        """
        date1 = timezone.now() + timezone.timedelta(days=4)
        date2 = timezone.now() + timezone.timedelta(days=3)
        date3 = timezone.now() + timezone.timedelta(days=2)
        date4 = timezone.now() + timezone.timedelta(days=1)
        ev1 = Event(name='Primavera Sound', state='SR', date=date1, description="Short Description", establishment=self.est[0])
        ev1.save()
        ev1.band.add(self.bands[1], self.bands[2])
        ev2 = Event(name='Acampada Jove', state='CL', date=date2, description="Short Description", establishment=self.est[1])
        ev2.save()
        ev2.band.add(self.bands[0], self.bands[3])
        ev3 = Event(name='Festiuet', state='SR', date=date3, description="Short Description", establishment=self.est[2])
        ev3.save()
        ev3.band.add(self.bands[0], self.bands[1])
        ev4 = Event(name='Ressurection fest', state='CL', date=date4, description="Short Description", establishment=self.est[3])
        ev4.save()
        ev4.band.add(self.bands[2], self.bands[3])
        self.events = [ev1, ev2, ev3, ev4]

