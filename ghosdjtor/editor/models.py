from django.db import models

# Create your models here.

class UploadedImage(models.Model):
    """ Model to track uploaded images """
    image = models.ImageField(upload_to='files/%Y/%m/%d')
