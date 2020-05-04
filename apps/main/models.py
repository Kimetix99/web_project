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
    web_link = models.URLField('Web Link to Portfolio', max_length=255)
    playlist = models.URLField('SoundCloud Playlist', max_length=300)
    email = models.CharField('A contact email', max_length=100)
    mobile = models.CharField('A mobile phone to contact you', max_length=16)
    image = models.ImageField('An image of the band', upload_to='img/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='band')

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

    name = models.CharField('Name of the Event', max_length=300, blank=True)
    band = models.ManyToManyField('Band', related_name='events', blank=True)
    state = models.CharField('State of the event', max_length=2, choices=STATE, default="SR")
    date = models.DateTimeField('Date of the event', null=False)
    description = models.TextField()
    establishment = models.ForeignKey('Establishment', on_delete=models.CASCADE, null=False, related_name='events')
    class Meta:
        permissions = [
                ('event_owner', 'User owner of the establishment owner of the Event'),
                ]  # Bands will contact privately to the owner, so it's not needed

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField('Establishment name', max_length=300, blank=True)
    address = models.CharField('Address', max_length=200)
    email = models.CharField('Email to contact you', max_length=100)
    mobile = models.CharField('Mobile phone to contact you', max_length=16)
    image = models.ImageField('An image of the establishment', upload_to='img/', default=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='establishments')

    class Meta:
        permissions = [
                ('establishment_owner', 'User owner of the establishement')]

    def __str__(self):
        return self.name


