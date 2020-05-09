from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Band
from django.urls import reverse

User = get_user_model()


class EditBandTest(TestCase):

    global band

    def setUp(self):
        user1 = get_user_model().objects.create_user(username='user', password='testpass123')
        self.band = Band.objects.create(name="itacaband", web_link='https://soundcloud.com/skeewiff',
                                        playlist='https://soundcloud.com/dj-elye/sets/jazz', email="skeewiff@gmail.com",
                                        mobile="000000000", user=user1)

    def test_band_edit_template(self):
        self.client.login(username='user', password='testpass123')
        self.response = self.client.get(reverse("band_edit", kwargs={'pk': self.band.pk}))
        self.assertEqual(self.response.status_code, 200)

    def test_not_login(self):
        self.response = self.client.get(reverse("band_edit", kwargs={'pk': self.band.pk}))
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '%s?next=%s' %
                (reverse('login'), reverse('band_edit', kwargs={'pk': self.band.pk}))
                )



