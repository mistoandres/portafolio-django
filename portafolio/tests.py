from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project

class ProfileTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_project_exists(self):
        pass

    def setUp(self):
        User.objects.create_user('test', 'Esta_es_una_prueba', 'https://www.google.com')

    def test_project_exists(self):
        exists = Project.objects.filter(user_username='test').exists()
        self.assertEqual(exists, True)
