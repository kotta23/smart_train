from django.db import models

# Create your models here.

class DisplayData(models.Model):
    first_name = models.CharField(max_length=30 ,blank=False)
    last_name = models.CharField(max_length=30)
    valu1 = models.FloatField()
    valu2 = models.FloatField()