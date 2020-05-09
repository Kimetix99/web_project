from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Band, Event, Establishment
from django.urls import reverse


User = get_user_model()

class ListEventTest(TestCase):

    def setUp(self):
        """
            Sets up a lot of infrastructure
        """
        user1 = User.objects.create_user(username="skewiff", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        user2 = User.objects.create_user(username="tessatioarina", password="testingpaco123", email="paco@gmail.co", first_name="Paco", last_name="Rodriguez")
        user3 = User.objects.create_user(username="drei-jazz", password="testingpaco123", email="paco@gmail.om", first_name="Paco", last_name="Rodriguez")
        user4 = User.objects.create_user(username="angelo-mikha", password="testingpaco123", email="paco@gmail.cm", first_name="Paco", last_name="Rodriguez")
        band1 = Band.objects.create(web_link='https://soundcloud.com/skeewiff', playlist='https://soundcloud.com/dj-elye/sets/jazz',      email="skeewiff@gmail.com", mobile="000000000", user=user1)
        band2 = Band.objects.create(web_link='https://soundcloud.com/tessatioarina', playlist='https://soundcloud.com/dj-elye/sets/jazz', email="tessatioarina@gmail.com", mobile="100000000", user=user2)
        band3 = Band.objects.create(web_link='https://soundcloud.com/drei-jazz', playlist='https://soundcloud.com/dj-elye/sets/jazz',     email="tessatioarina@gmail.com", mobile="200000000", user=user3)
        band4 = Band.objects.create(web_link='https://soundcloud.com/angelo-mikha', playlist='https://soundcloud.com/dj-elye/sets/jazz',  email="angelo@gmail.com", mobile="300000000", user=user4)
        user5 = User.objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        user6 = User.objects.create_user(username="paquito1", password="testingpaco123", email="paco@gmail.co", first_name="Paco", last_name="Rodriguez")
        user7 = User.objects.create_user(username="paquito2", password="testingpaco123", email="paco@gmail.om", first_name="Paco", last_name="Rodriguez")
        user8 = User.objects.create_user(username="paquito3", password="testingpaco123", email="paco@gmail.cm", first_name="Paco", last_name="Rodriguez")
        date1 = timezone.now() + timezone.timedelta(days=4)
        date2 = timezone.now() + timezone.timedelta(days=3)
        date3 = timezone.now() + timezone.timedelta(days=2)
        date4 = timezone.now() + timezone.timedelta(days=1)
        est1 = Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=user5)
        est2 = Establishment.objects.create(name="Bar Pac2", address="C/Major n9", email="paco96@gmail.com", mobile="100000000", user=user6)
        est3 = Establishment.objects.create(name="Bar Pac3", address="C/Major n9", email="paco96@gmail.com", mobile="200000000", user=user7)
        est4 = Establishment.objects.create(name="Bar Pac4", address="C/Major n9", email="paco96@gmail.com", mobile="300000000", user=user8)
        ev1 = Event(name='Primavera Sound', state='SR', date=date1, description="Short Description", user=user5)
        ev1.save()
        ev1.band.add(band2, band3)
        ev2 = Event(name='Acampada Jove', state='CL', date=date2, description="Short Description", user=user6)
        ev2.save()
        ev2.band.add(band1, band4)
        ev3 = Event(name='Festiuet', state='SR', date=date3, description="Short Description", user=user7)
        ev3.save()
        ev3.band.add(band1, band2)
        ev4 = Event(name='Ressurection fest', state='CL', date=date4, description="Short Description", user=user8)
        ev4.save()
        ev4.band.add(band3, band4)



    def test_events_list(self):
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Primavera Sound")
        self.assertContains(response, "Acampada Jove")
        self.assertContains(response, "Festiuet")
        self.assertContains(response, "Ressurection fest")
        self.assertTemplateUsed(response, 'event/list.html')
        self.assertTemplateUsed(response, '_base.html')


