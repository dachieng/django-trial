from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length = 100)
    image:models.ImageField(upload_to = 'pics')
    age: models.IntegerField()
    description:models.TextField(max_length=200)
    offer:models.BooleanField(default=False)