from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='team')
    desc = models.TextField()

    def __str__(self):
        return self.first_name

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='place')
    description = models.TextField()

    def __str__(self):
        return self.name