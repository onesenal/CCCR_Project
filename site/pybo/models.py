from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class world(models.Model):
    CONTINENT = models.CharField(max_length=100)
    COUNTRY = models.CharField(max_length=100)

    
