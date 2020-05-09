from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Establishment, Band, Event
from django.urls import reverse

User = get_user_model()


class EditEventTest(TestCase):

    global band

    def setUp(self):
        user1 = get_user_model().objects.create_user(username='user', password='testpass123')
        date1 = timezone.now() + timezone.timedelta(days=4)
        est1 = Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com",
                                            mobile="000000000", user=user1)
        self.ev1 = Event.objects.create(name='Primavera Sound', state='SR', date=date1, description="Short Description",
                         establishment=est1)

    def test_event_edit_template(self):
        self.client.login(username='user', password='testpass123')
        self.response = self.client.get(reverse("event_edit", kwargs={'pk': self.ev1.pk}))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed('event/edit.html')
        self.assertTemplateUsed('_base.html')

    def test_not_login(self):
        self.response = self.client.get(reverse("event_edit", kwargs={'pk': self.ev1.pk}))
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '%s?next=%s' %
                (reverse('login'), reverse('event_edit', kwargs={'pk': self.ev1.pk}))
                )