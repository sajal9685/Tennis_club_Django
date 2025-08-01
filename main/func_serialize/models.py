from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    branch= models.CharField(max_length=255)

    def __str__(self):
        return self.firstname
    
