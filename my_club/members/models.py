from django.db import models

class Destination(models.Model):
  name=models.CharField(max_length=200)
  img=models.ImageField(upload_to='destination_images/')
  dest=models.CharField(max_length=200)
  price=models.IntegerField()
