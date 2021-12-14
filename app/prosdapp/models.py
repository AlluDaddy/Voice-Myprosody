from django.db import models

# Create your models here.
class Voice(models.Model):
    voice_record = models.FileField()