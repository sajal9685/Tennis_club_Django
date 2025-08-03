from django.db import models

# Create your models here.

class Family(models.Model):
    headName= models.CharField(max_length=50)
    members = models.IntegerField()

    def __str__(self):
        return self.headName   