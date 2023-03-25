from django.db import models
from django.urls import reverse

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = f'/{self.name}'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(self.url)