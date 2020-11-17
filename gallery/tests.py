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

# class ImageTest(TestCase):
#     """
#     Class for testing Image model.

#     Args:
#         TestCase: Inherits from class TestCase
#     """
#     def setUp(self):
#         """
#         Runs before each test case
#         """
#         self.place = Location.objects.create(city = "place", country = "Kenya")
#         self.cityscape = Category.objects.create(category = "cityscape")

#         self.new_image = Image(image = "/static/images/city.png", name = "city", description = "A wonderful portrait of place city", location = self.place, category = self.cityscape)

#     def tearDown(self):
#         """
#         Runs after each test case
#         """