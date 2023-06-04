from django.db import models

# Create your models here.
class Livreur(models.Model):
    name = models.CharField(max_length=255)
    Created = models.DateTimeField('auto_now_add=True')
    