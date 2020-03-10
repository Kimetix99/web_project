from django.contrib import admin
from apps.main import models
# Register your models here.

admin.site.register(models.Band)
admin.site.register(models.Event)
admin.site.register(models.Establishment)