from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Establishment
from django.urls import reverse

User = get_user_model()


class ListEstablishmentTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        establishment = Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=user1)


    def test_establishment_list(self):
        response = self.client.get(reverse('{% url establishment_detail establishment.pk %}'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bar Pac1')
        self.assertTemplateUsed(response, 'establishment/detail.html')
        self.assertTemplateUsed(response, '_base.html')
