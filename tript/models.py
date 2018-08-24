from django.db import models
from django.contrib import auth

# Create your models here.
class TriptUser(auth.models.User, auth.models.PermissionsMixin):
   ## user = models.OneToOneField(User)
   ## country = models.CharField(max_length=256)
   ## city = models.CharField(max_length=256)

    def __str__(self):
        return self.username

class Trips(models.Model):
    countries = models.CharField(max_length=256)
    cities= models.CharField(max_length=256)
