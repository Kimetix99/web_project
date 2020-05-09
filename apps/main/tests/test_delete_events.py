from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Band, Event, Establishment
from django.urls import reverse
class DeleteEventTest(TestCase):

    def setUp(self):
        user1 = get_user_model().objects.create_user(username="skewiff", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        band1 = Band.objects.create(name="itacaband", web_link='https://soundcloud.com/skeewiff', playlist='https://soundcloud.com/dj-elye/sets/jazz',      email="skeewiff@gmail.com", mobile="000000000", user=user1)
        user5 = get_user_model().objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        date1 = timezone.now() + timezone.timedelta(days=4)
        est1 = Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=user5)
        self.ev1 = Event.objects.create(name='Primavera Sound', state='SR', date=date1, description="Short Description", establishment=est1)
        get_user_model().objects.create_user(username='user', password='testpass123')

    def test_event_delete_template_user_no_match(self):
        self.client.login(username='user', password='testpass123')
        response = self.client.get(reverse("event_delete", kwargs={'pk':self.ev1.pk}))
        self.assertEqual(response.status_code, 403)

    def test_event_delete_template_user_match(self):
        self.client.login(username='paquito', password='testingpaco123')
        response = self.client.get(reverse("event_delete", kwargs={'pk':self.ev1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Primavera Sound')
        self.assertTemplateUsed(response, 'event/confirm_delete.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_delete_event(self):
        self.client.login(username='paquito', password='testingpaco123')
        num_before = len(Event.objects.all())
        response = self.client.post(reverse("event_delete", kwargs={'pk':self.ev1.pk}))
        num_after = len(Event.objects.all())
        self.assertNotEqual(num_before, num_after)

    def test_not_login(self):
        self.response = self.client.get(reverse("event_delete", kwargs={'pk':self.ev1.pk}))
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '%s?next=%s' % 
                (reverse('login'), reverse("event_delete", kwargs={'pk':self.ev1.pk}))
                )


