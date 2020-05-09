from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.main.models import Band

class DeleteBandTest(TestCase):

    def setUp(self):
        user1 = get_user_model().objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        self.band = Band.objects.create(name="itacaband", web_link='https://soundcloud.com/skeewiff', playlist='https://soundcloud.com/dj-elye/sets/jazz', email="skeewiff@gmail.com", mobile="000000000", user=user1)
        get_user_model().objects.create_user(username='user', password='testpass123')

    def test_band_delete_template_user_no_match(self):
        self.client.login(username='user', password='testpass123')
        response = self.client.get(reverse("band_delete", kwargs={'pk':self.band.pk}))
        self.assertEqual(response.status_code, 403)
    
    def test_band_delete_template_user_match(self):
        self.client.login(username='paquito', password='testingpaco123')
        response = self.client.get(reverse("band_delete", kwargs={'pk':self.band.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'itacaband')
        self.assertTemplateUsed(response, 'band/confirm_delete.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_delete_band(self):
        self.client.login(username='paquito', password='testingpaco123')
        num_before = len(Band.objects.all())
        response = self.client.post(reverse("band_delete", kwargs={'pk':self.band.pk}))
        num_after = len(Band.objects.all())
        self.assertNotEqual(num_before, num_after)

    def test_not_login(self):
        self.response = self.client.get(reverse("band_delete", kwargs={'pk':self.band.pk}))
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '%s?next=%s' % 
                (reverse('login'), reverse("band_delete", kwargs={'pk':self.band.pk}))
                )


