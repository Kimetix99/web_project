from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Establishment
from django.urls import reverse

User = get_user_model()


class ListEstablishmentTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        user2 = User.objects.create_user(username="paquito1", password="testingpaco123", email="paco@gmail.co", first_name="Paco", last_name="Rodriguez")
        user3 = User.objects.create_user(username="paquito2", password="testingpaco123", email="paco@gmail.om", first_name="Paco", last_name="Rodriguez")
        user4 = User.objects.create_user(username="paquito3", password="testingpaco123", email="paco@gmail.cm", first_name="Paco", last_name="Rodriguez")
        Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=user1)
        Establishment.objects.create(name="Bar Pac2", address="C/Major n9", email="paco96@gmail.com", mobile="100000000", user=user2)
        Establishment.objects.create(name="Bar Pac3", address="C/Major n9", email="paco96@gmail.com", mobile="200000000", user=user3)
        Establishment.objects.create(name="Bar Pac4", address="C/Major n9", email="paco96@gmail.com", mobile="300000000", user=user4)


    def test_establishment_list(self):
        response = self.client.get(reverse('establishment_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bar Pac1')
        self.assertContains(response, 'Bar Pac2')
        self.assertContains(response, 'Bar Pac3')
        self.assertContains(response, 'Bar Pac4')
        self.assertTemplateUsed(response, 'establishment/list.html')
        self.assertTemplateUsed(response, '_base.html')
