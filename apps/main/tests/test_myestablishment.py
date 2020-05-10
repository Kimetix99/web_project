from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Establishment
from django.urls import reverse

User = get_user_model()


class MyEstablishmentTest(TestCase):


    def setUp(self):
        self.user1 = User.objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")


    def test_establishment_detail(self):
        self.client.login(username='paquito', password='testingpaco123')
        self.establishment = Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=self.user1)
        response = self.client.get(reverse("myestablishment"))
        self.assertEqual(response.status_code, 302)


    def test_establishment_create(self):
        self.client.login(username='paquito', password='testingpaco123')
        self.response = self.client.get(reverse("myestablishment"))
        self.assertEqual(self.response.status_code, 302)
