from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name



      #  img = Image.open(self.picture.path)

      #  if img.height > 600 or img.width > 600:
      #     output_size = (600, 600)
      #      img.thumbnail(output_size)
      #      img.save(self.picture.path)

