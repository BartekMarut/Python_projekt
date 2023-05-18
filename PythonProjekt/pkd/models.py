from django.db import models

class Pkd(models.Model):
  pkdNumber = models.CharField(max_length=255)
  pkdDesc = models.CharField(max_length=255)