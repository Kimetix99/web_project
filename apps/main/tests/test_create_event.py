"""
Credits to Navy
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.main.models import Establishment


class CreateEventsTest(TestCase):

    def setUp(self):
        self.url = reverse('event_create')
        self.user = get_user_model().objects.create_user(username='user', password='testpass123')

    def test_event_create_template(self):
        self.client.login(username='user', password='testpass123')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 403)

    def test_not_login(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '%s?next=%s' %
                             (reverse('login'), reverse('event_create')))

    def test_has_establishment(self):
        est = Establishment.objects.create(user=self.user, name='bar paco', address='carrer de lamargura',
                email='b@b.c', mobile='234567')
        self.client.login(username='user', password='testpass123')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'event/create.html')
        self.assertTemplateUsed(self.response, '_base.html')
