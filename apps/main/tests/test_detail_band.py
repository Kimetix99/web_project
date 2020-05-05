from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Band
from django.urls import reverse

User = get_user_model()


class DetailBandTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        band = Band.objects.create(name="itacaband", web_link='https://soundcloud.com/skeewiff', playlist='https://soundcloud.com/dj-elye/sets/jazz',      email="skeewiff@gmail.com", mobile="000000000", user=user1)


    def test_bands_list(self):
        response = self.client.get(reverse('{% url band_detail band.pk %}'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "skeewiff@gmail.com")
        self.assertTemplateUsed(response, 'band/detail.html')
        self.assertTemplateUsed(response, '_base.html')