from django.test import TestCase
from .models import Order,Pet


# Create your tests here.
class UserTestCase(TestCase):
    def OrderTest(self):
        self.petid = Pet.objects.create(
            id = self,

        ) 
        self.user = Order.objects.create(
            name="DogSale",
            petId="",
            quantity="Pass12345",
            shipDate="Javohir",
            status="Rustamov",
            complete="Fals"
        )

    def test_user(self):
        self.assertEqual(self.user.username, "test")
        self.assertEqual(self.user.email, "test@gmail.com")
        self.assertEqual(self.user.password, "Pass12345")
        self.assertEqual(self.user.firstName, "Javohir")
        self.assertEqual(self.user.lastName, "Rustamov")

