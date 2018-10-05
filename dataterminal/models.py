from django.db import models

# Create your models here.

class FieldMap(models.Model):
    name=models.CharField(max_length=20)

class FieldStudy(models.Model):
    name=models.CharField(max_length=20)
    


