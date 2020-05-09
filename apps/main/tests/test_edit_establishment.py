from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.main.models import Establishment
from django.urls import reverse

User = get_user_model()


class EditEstablishmentTest(TestCase):

    global band

    def setUp(self):
        user1 = get_user_model().objects.create_user(username='user', password='testpass123')
        self.establishment = Establishment.objects.create(name="Bar Pac1", address="C/Major n9",
                                                          email="paco96@gmail.com", mobile="000000000", user=user1)

    def test_establishment_edit_template(self):
        self.client.login(username='user', password='testpass123')
        self.response = self.client.get(reverse("establishment_edit", kwargs={'pk': self.establishment.pk}))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed('establishment/edit.html')
        self.assertTemplateUsed('_base.html')

    def test_not_login(self):
        self.response = self.client.get(reverse("establishment_edit", kwargs={'pk': self.establishment.pk}))
        self.assertEqual(self.response.status_code, 302)
        self.assertRedirects(self.response, '%s?next=%s' %
                (reverse('login'), reverse('establishment_edit', kwargs={'pk': self.establishment.pk}))
                )