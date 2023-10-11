from django.db import models

# Create your models here.
class Sketch(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(default='')

    def __str__(self):
        return self.name