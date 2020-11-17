from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Location(models.Model):
    """
    Class to define location instances
    Args:
        models.Model: Inherits from models.Model class
    """
    city = models.CharField(max_length = 150)
    country = models.CharField(max_length = 150)
    
    @property
    def location(self):
        """
        Combines city and country into new location property
        """
        return f"{self.city}, {self.country}"

    def save_location(self):
        """
        Saves location to database
        """
        self.save()

    def update_location(self, city, country):
        """
        Method to change location values
        """
        self.city = city
        self.country = country
        self.save_location()

    def delete_location(self):
        """
        Method to remove location from database
        """
        self.delete()

    def __str__(self):
        return self.location(self)

class Categories(models.Model):
    """
    Class to define category instances
    Args:
        models.Model: Inherits from models.Model class
    """
    category = models.CharField(max_length = 50)

    def save_category(self):
        """
        Saves category to database
        """
        self.save()

    def update_category(self, category):
        """
        Method to change category values
        """
        self.category = category
        self.save_category()

    def delete_category(self):
        """
        Method to remove category from database
        """
        self.delete()

    def __str__(self):
        return self.category

class Image(models.Model):
    """
    Class to define image instances
    Args:
        models.Model: Inherits from models.Model class
    """
    image = CloudinaryField("image")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length = 280)
    location = models.ForeignKey(Location, on_delete = models.PROTECT)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.name