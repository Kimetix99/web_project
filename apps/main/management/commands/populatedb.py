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
        band1 = Band.objects.create(name="itacaband", web_link='https://www.itacaband.com/', playlist='https://open.spotify.com/embed/artist/1tQtaouRCs37gaJVi7HTYR',email="itacaband@hotmail.com", mobile="656 184 240", user=self.users[0], image="/bands/itaca.jpeg")
        band2 = Band.objects.create(name="metallica", web_link='https://www.metallica.com/', playlist='https://open.spotify.com/embed/artist/2ye2Wgw4gimLv2eAKyk1NB', email="metallica@gmail.com", mobile="640 319 304", user=self.users[1], image="/bands/metallica.jpeg" )
        band3 = Band.objects.create(name="Maravillosa Orquesta del Alchol", web_link='http://www.lamaravillosaorquestadelalcohol.com/', playlist='https://open.spotify.com/embed/artist/1vBn5Puz4mdZopZEHq1QDq', email="grupo@lamaravillosaorquestadelalcohol.com", mobile="650 193 472", user=self.users[2] , image="/bands/orquesta.jpeg" )
        band4 = Band.objects.create(name="Oques Grasses", web_link='http://oquesgrasses.com/', playlist='https://open.spotify.com/embed/artist/5qPeAT4ikl6gJNUexAOEy0',  email="jordi@fourni.org", mobile="617 351 623", user=self.users[3], image="/bands/oques.jpg" )
        self.bands = [band1, band2, band3, band4]


    def _create_establishment(self):
        """
        Creates all the establishments.
        """
        est1 = Establishment.objects.create(name="La Cosmopolita", address="Málaga Centro n2", email="lacosmopolita@gmail.com", mobile="952 21 58 27", user=self.users[4], image="/establishments/e1.jpeg")
        est2 = Establishment.objects.create(name="Izakaya Kobachi", address="Calle nevot 26, Granada", email="izakaya@gmail.com", mobile="958 21 07 09", user=self.users[5], image="/establishments/e2.jpeg")
        est3 = Establishment.objects.create(name="Canalla Bistró", address="Calle de Goya, 5-7, 28001 Madrid", email="canallabistro@gmail.com", mobile="91 577 00 25", user=self.users[6], image="/establishments/e3.jpeg")
        est4 = Establishment.objects.create(name="Casa Paco", address="Calle Mayor n1", email="paco96@gmail.com", mobile="973444000", user=self.users[7], image="/establishments/e4.jpeg")
        self.est = [est1, est2, est3, est4]

        
        

    def _create_events(self):
        """
        Creates all the events needed.
        """
        date1 = timezone.now() + timezone.timedelta(days=4)
        date2 = timezone.now() + timezone.timedelta(days=3)
        date3 = timezone.now() + timezone.timedelta(days=2)
        date4 = timezone.now() + timezone.timedelta(days=1)
        ev1 = Event(name='Primavera Sound', state='SR', date=date1, description="The nature of the festival (urban and an integrated part of the city) and the wide range of bands represented have made Primavera Sound a meeting point for artists and spectators from all generations.", user=self.users[4])
        ev1.save()
        ev1.band.add(self.bands[1], self.bands[2])
        ev2 = Event(name='Acampada Jove', state='CL', date=date2, description="L'Acampada Jove és el festival político-musical de referència dels Països Catalans.", user=self.users[5])
        ev2.save()
        ev2.band.add(self.bands[0], self.bands[3])
        ev3 = Event(name='Festiuet', state='SR', date=date3, description="Festiuet is a multi-genre music festival in Spain. Its recent lineups have included Berri Txarrak, Desakato, Zoo and much more.", user=self.users[6])
        ev3.save()
        ev3.band.add(self.bands[0], self.bands[1])
        ev4 = Event(name='Ressurection fest', state='CL', date=date4, description="This festival is held annually since 2006 during July or early August, and features mainly heavy metal, hardcore punk and punk rock bands", user=self.users[7])
        ev4.save()
        ev4.band.add(self.bands[2], self.bands[3])
        self.events = [ev1, ev2, ev3, ev4]

