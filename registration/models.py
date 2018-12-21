from django.db import models


# Modelo User, de django
from django.contrib.auth.models import User

class Profile(models.Model):
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(verbose_name='Biografia')
    link = models.URLField(max_length=200, null=True, blank=True)

    #Relación de uno a uno (User 1 - 1 Profile)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
