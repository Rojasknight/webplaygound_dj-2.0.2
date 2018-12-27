from django.test import TestCase

# Profile model.
from .models import Profile

# User model - django.
from django.contrib.auth.models import User


# Create your tests here.

class ProfileTestCase(TestCase):

    def setUp(self):
        ''' Creamos el usuario, con su perfil'''
        User.objects.create_user('test', 'test@mail.com', 'test1234')

    def test_profile_exist(self):
        '''Validamos que el perfil exista'''
        exist = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exist, True)
