from django.db import models

class Developer(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Years = models.SmallIntegerField(null=True)
