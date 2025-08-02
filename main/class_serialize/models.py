from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    designation= models.CharField(max_length=255)

    def __str__(self):
        return self.firstname
    
