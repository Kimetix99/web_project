from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Band, Event, Establishment
from django.urls import reverse


User = get_user_model()

class ListEstablishmentTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username="skewiff", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        band1 = Band.objects.create(web_link='https://soundcloud.com/skeewiff', playlist='https://soundcloud.com/dj-elye/sets/jazz',      email="skeewiff@gmail.com", mobile="000000000", user=user1)
        user5 = User.objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        date1 = timezone.now() + timezone.timedelta(days=4)
        est1 = Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=user5)
        ev1 = Event(name='Primavera Sound', state='SR', date=date1, description="Short Description", establishment=est1)
        ev1.save()



    def test_events_list(self):
        response = self.client.get(reverse('{% url event_detail ev1.pk %}'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Primavera Sound")
        self.assertTemplateUsed(response, 'event/detail.html')
        self.assertTemplateUsed(response, '_base.html')


