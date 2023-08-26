from django.test import TestCase
from utils.choices import PetStatusChoices
# Create your tests here.
from django.test import TestCase

from .models import Tag, Category, Pet, Image


# Create your tests here.
class TagTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name = "Pets",
        )

    def test_tag(self):
        self.assertEqual(self.tag.name, "Pets")


class CategoryTestCase(TestCase):
    def setUp(self):
        self.parent = Category.objects.create(
            name = "Vhicle",
        )
        self.category = Category.objects.create(
            name = "Cars",
        )

    def test_tag(self):
        self.assertEqual(self.category.name, "Cars")
        self.assertEqual(self.category.parent, self.parent)


class PetTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name = "Auto",
        )
        self.tags = Tag.objects.create(
            name = 'Transport',
        )
        self.status = PetStatusChoices.PENDING
        self.photoUrls =  Image.objects.create(
            name = 'Cat',
            image = 'url'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!,
            is_main = 'False',

        )
        self.pet= Pet.objects.create(
            name = "Pets",
            category = self.category,
            tags = self.tags ,
            status = self.status,
            photoUrls = self.photoUrls,
   
        )

    def test_tag(self):
        self.assertEqual(self.pet.name, "Pets")
        self.assertEqual(self.category.name, "Auto")
        self.assertEqual(self.tags.name, "Transport")
        self.assertEqual(self.status, "PENDING")
        self.assertEqual(self.photoUrls.name, 'Cat')
        self.assertEqual(self.photoUrls.image, '$$$$$$$$')
        self.assertEqual(self.photoUrls.is_main, 'False')






class MyModelTestCase(TestCase):
    def test_photo_url(self):
        # Create a test object with a photo URL
        my_object = MyModel.objects.create(name='Test Object', photo_url='http://example.com/photo.jpg')

        # Retrieve the object from the database
        saved_object = MyModel.objects.get(pk=my_object.pk)

        # Assert that the retrieved object's photo URL matches the expected URL
        self.assertEqual(saved_object.photo_url, 'http://example.com/photo.jpg')
