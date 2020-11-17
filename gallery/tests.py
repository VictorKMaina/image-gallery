from django.test import TestCase
from .models import *

class LocationTest(TestCase):
    """
    Class for testing Location model.

    Args:
        TestCase: Inherits from class TestCase
    """
    def setUp(self):
        """
        Runs before each test case.
        """
        self.place = Location(city = "Nairobi", country = "Kenya")

    def tearDown(self):
        """
        Runs after each test case
        """
        Location.objects.all().delete()

    def test_location_instance(self):
        """
        Test case for checking if Location instance is created
        """
        self.place.save()
        self.assertTrue(isinstance(self.place, Location))

    def test_location_method(self):
        """
        Test case for checking if method combines city and country into locaiton
        """
        self.assertEqual(self.place.location, "Nairobi, Kenya")

    def test_save_location(self):
        """
        Test case for checking if save_location method adds location to database
        """
        self.place.save_location()
        locations = Location.objects.all()

        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        """
        Test case for checking if update_location method changes value of city and country
        """
        self.place.save_location()
        self.place.update_location("Kampala", "Uganda")

        self.assertEqual(self.place.city, "Kampala")
        self.assertEqual(self.place.country, "Uganda")

    def test_delete_location(self):
        """
        Test case for checking if delete_location method deletes location from database
        """
        self.place.save_location()
        self.place.delete_location()

        locations = Location.objects.all()

        self.assertTrue(len(locations) == 0)

class CategoriesTest(TestCase):
    """
    Class for testing Categories model.

    Args:
        TestCase: Inherits from class TestCase
    """
    def setUp(self):
        """
        Runs before each test case.
        """
        self.category = Categories(category = "cityscape")

    def tearDown(self):
        """
        Runs after each test case
        """
        Categories.objects.all().delete()

    def test_category_instance(self):
        """
        Test case for checking if Categories instance is created
        """
        self.assertTrue(isinstance(self.category, Categories))

    def test_save_category(self):
        """
        Test case for checking if save_category method adds category to database
        """
        self.category.save_category()
        categories = Categories.objects.all()

        self.assertTrue(len(categories) > 0)

    def test_update_category(self):
        """
        Test case for checking if update_category method changes value of city and country
        """
        self.category.save_category()
        self.category.update_category("wildlife")

        self.assertEqual(self.category.category, "wildlife")

    def test_delete_category(self):
        """
        Test case for checking if delete_category method deletes category from database
        """
        self.category.save_category()
        self.category.delete_category()

        categories = Categories.objects.all()

        self.assertTrue(len(categories) == 0)

class ImageTest(TestCase):
    """
    Class for testing Image model.

    Args:
        TestCase: Inherits from class TestCase
    """
    def setUp(self):
        """
        Runs before each test case
        """
        self.location = Location.objects.create(city = "Nairobi", country = "Kenya")
        self.category = Categories.objects.create(category = "cityscape")

        self.new_image = Image(image = "/static/images/city.png", name = "Nairobi City", description = "A wonderful portrait of the city of Nairobi", location = self.location)

    def tearDown(self):
        """
        Runs after each test case
        """
        Location.objects.all().delete()
        Categories.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        """
        Test case to check if self.new_image is instance of Image class
        """
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        """
        Test case for checking if save_image method adds image to database
        """
        self.new_image.save_image()
        images = Image.objects.all()

        self.assertTrue(len(images) > 0)

    def test_update_image(self):
        """
        Test case for checking if update_image method changes value image.image
        """
        self.new_image.save_image()
        self.new_image.update_image("/static/images/lion.jpg")

        self.assertEqual(self.new_image.image, "/static/images/lion.jpg")

    def test_delete_image(self):
        """
        Test case for checking if delete_image method deletes image from database
        """
        self.new_image.save_image()
        self.new_image.delete_image()

        images = Image.objects.all()

        self.assertTrue(len(images) == 0)

    def test_add_new_category(self):
        """
        Test case to check if add_category method adds category to image.categories
        """
        self.new_image.save_image()
        self.new_image.add_category(self.category)

        self.assertEqual(len(self.new_image.categories) > 0)