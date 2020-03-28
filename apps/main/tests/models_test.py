from django.test import TestCase
from django.contrib.auth.models import User
from apps.main.models import Band, Event, Establishment
import datetime

# Create your tests here.
class Establishment_Test(TestCase):
    
    def setUp(self):
        user1 = User.objects.create(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        Establishment.objects.create(name="Bar Paco", address="C/Major n9", contacte_email="paco96@gmail.com", contacte_mobil="000000000", image="profile.png", owner=user1)

    def insert_establishment(self):
        establishment_query = Establishment.objects.get(name="Bar Paco")
        self.assertEqual("Bar Paco", establishment_query.name)

    def delete_establishment(self):
        Establishment.objects.filter(name="Bar Paco").delete()
        establishment = Establishment.objects.filter(name="Bar Paco")
        self.assertEquals(0, len(establishment))

class Event_Test(TestCase):

    def setUp(self):
        now = datetime.datetime.now()
        user2 = User.objects.create(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        establishment = Establishment.objects.create(name="Bar Paco", address="C/Major n9", contacte_email="paco96@gmail.com", contacte_mobil="000000000", image="profile.png", owner=user2)
        Event.objects.create(name="Primavera Sound", date=now, description="Festival de música", establishment=establishment)

    def insert_event(self):
        event_query = Event.objects.get(name="Primavera Sound")
        self.assertEqual("Primavera Sound", event_query.name)
    
    def insert_band_into_event(self):
        user1 = User.objects.create(username="aspencat", password="testingaspencat123", email="aspencat@gmail.com", first_name="Aspencat", last_name="Band")
        band = Band.objects.create(web_link = "http://aspencat.org/", playlist="https://soundcloud.com/aspencat/escriurem-mil-batalles", contacte_email="aspencat@gmail.com", contacte_mobil="000000000", image="perfil.png", idUser=user1)
        event = Event.objects.get(name="Primavera Sound")
        event.band.add(band)
        self.assertTrue(event.band.filter(idUser=User.objects.get(username="aspencat")).exists())

    def delete_event(self):
        Event.objects.filter(name="Primavera Sound").delete()
        events = Event.objects.filter(name="Primavera Sound")
        self.assertEqual(0, len(events))

class Band_Test(TestCase):

    def setUp(self):
        user1 = User.objects.create(username="aspencat", password="testingaspencat123", email="aspencat@gmail.com", first_name="Aspencat", last_name="Band")
        Band.objects.create(web_link = "http://aspencat.org/", playlist="https://soundcloud.com/aspencat/escriurem-mil-batalles", contacte_email="aspencat@gmail.com", contacte_mobil="000000000", image="perfil.png", idUser=user1)
    
    def insert_band(self):
        band_query = Band.objects.get(idUser=User.objects.get(username="aspencat"))
        self.assertEqual("aspencat", band_query.idUser.username)

    def delete_band(self):
        Band.objects.filter(idUser=User.objects.get(username="aspencat")).delete()
        band = Band.objects.filter(idUser=User.objects.get(username="aspencat"))
        self.assertEqual(0, len(band))