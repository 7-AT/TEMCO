from datetime import datetime
from sqlite3 import Date
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    cname = models.CharField(max_length=100)
    role = models.CharField(max_length=15)
    query = models.TextField()
    def __str__(self):
        return self.name 
# Create your models here.
