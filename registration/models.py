from django.db import models

# Modelo User, de django
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Optimizando el almacen del avatar
def custom_updaload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    avatar = models.ImageField(upload_to=custom_updaload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    # Relación de uno a uno (User 1 - 1 Profile)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# Crear el perfil del usuario despues de guardado
@receiver(post_save, sender=User)
def ensure_profile_exist(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print('Se acaba de crear el usuario y el perfil enlazado')
