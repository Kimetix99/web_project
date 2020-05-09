from django.forms import ModelForm
from apps.main import models


class EstablishmentForm(ModelForm):
    class Meta:
        model = models.Establishment
