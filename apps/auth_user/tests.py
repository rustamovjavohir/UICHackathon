from django.test import TestCase

from apps.auth_user.models import User


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            email="test@gmail.com",
            password="Pass12345",
            firstName="Javohir",
            lastName="Rustamov",
        )

    def test_user(self):
        self.assertEqual(self.user.username, "test")
        self.assertEqual(self.user.email, "test@gmail.com")
        self.assertEqual(self.user.password, "Pass12345")
        self.assertEqual(self.user.firstName, "Javohir")
        self.assertEqual(self.user.lastName, "Rustamov")
