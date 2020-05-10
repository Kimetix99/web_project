"""
Credits to Navy
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.main.models import Establishment


class CreateEstablishmentTest(TestCase):

    def setUp(self):
        self.url = reverse('establishment_create')
        get_user_model().objects.create_user(username='user', password='testpass123')

    def test_establishment_create_template(self):
        self.client.login(username='user', password='testpass123')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'establishment/create.html')
        self.assertTemplateUsed(self.response, '_base.html')

    def test_not_login(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '%s?next=%s' %
                             (reverse('login'), reverse('establishment_create')))

