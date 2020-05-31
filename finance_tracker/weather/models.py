from django.db import models
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("weather:home")
    class Meta:
         verbose_name_plural = 'cities'
   