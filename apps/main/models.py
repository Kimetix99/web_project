"""
Models of the web app:
    Permissions will be handled by the module guardian,
    this lets us use the User authentication provided by
    Django and use object level permissions without changing
    the code. Guardian handles this permissions levels at 
    view code.
"""


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Band(models.Model):
    web_link = models.URLField(max_length=255)
    playlist = models.URLField(max_length=300)
    contacte_email = models.CharField(max_length=100)
    contacte_mobil = models.CharField(max_length=16)
    image = models.ImageField(upload_to='img/', blank=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='band')
    class Meta:
        permissions = [
                ('band_owner', 'User is the owner of the band'),
                ]

    def get_absolute_url(self):
        return reverse('band_detail', kwargs={'pk':self.pk})

class Event(models.Model):
    STATE = [
        ("SR", "Searching"),
        ("CL", "Closed"),
        ("FN", "Finalized")
    ]

    name = models.CharField(max_length=300, blank=True)
    band = models.ManyToManyField('Band', related_name='events', blank=True)
    state = models.CharField(max_length=2, choices=STATE, default="SR")
    date = models.DateTimeField(null=False)
    description = models.TextField()
    establishment = models.ForeignKey('Establishment', on_delete=models.CASCADE, null=False, related_name='events')
    class Meta:
        permissions = [
                ('event_owner', 'User owner of the establishment owner of the Event'),
                ]  # Bands will contact privately to the owner, so it's not needed

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=200)
    contacte_email = models.CharField(max_length=100)
    contacte_mobil = models.CharField(max_length=16)
    image = models.ImageField(upload_to='img/', default=None, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='establishments')

    class Meta:
        permissions = [
                ('establishment_owner', 'User owner of the establishement')]

    def __str__(self):
        return self.name


