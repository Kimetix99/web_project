from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.main.models import Establishment

class DeleteEstablishmentTest(TestCase):

    def setUp(self):
        user1 = get_user_model().objects.create_user(username="paquito", password="testingpaco123", email="paco@gmail.com", first_name="Paco", last_name="Rodriguez")
        self.establishment = Establishment.objects.create(name="Bar Pac1", address="C/Major n9", email="paco96@gmail.com", mobile="000000000", user=user1)
        get_user_model().objects.create_user(username='user', password='testpass123')

    def test_establishment_delete_template_user_no_mach(self):
        self.client.login(username='user', password='testpass123')
        response = self.client.get(reverse("establishment_delete", kwargs={'pk':self.establishment.pk}))
        self.assertEqual(response.status_code, 403)

    def test_establishment_delete_template_user_mach(self):
        self.client.login(username='paquito', password='testingpaco123')
        response = self.client.get(reverse("establishment_delete", kwargs={'pk':self.establishment.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bar Pac1')
        self.assertTemplateUsed(response, 'establishment/confirm_delete.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_delete_establishment(self):
        self.client.login(username='paquito', password='testingpaco123')
        num_before = len(Establishment.objects.all())
        response = self.client.post(reverse("establishment_delete", kwargs={'pk':self.establishment.pk}))
        num_after = len(Establishment.objects.all())
        self.assertNotEqual(num_before, num_after)

    def test_not_login(self):
        self.response = self.client.get(reverse("establishment_delete", kwargs={'pk':self.establishment.pk}))
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '%s?next=%s' % 
                (reverse('login'), reverse("establishment_delete", kwargs={'pk':self.establishment.pk}))
                )


