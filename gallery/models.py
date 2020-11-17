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
    location = models.CharField(max_length = 200, editable = False)

    def save(self, *args, **kwargs):
        self.location = f"{self.city}, {self.country}"
        super(Location, self).save(*args, **kwargs)

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
        self.location = f"{city}, {country}"
        self.save_location()

    def delete_location(self):
        """
        Method to remove location from database
        """
        self.delete()

    def __str__(self):
        print("LOCATION: ", self.location)
        return self.location

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

    @classmethod
    def search_images(cls, search_term):
        """
        Method that returns QuerySet of images that have a matching category name
        """
        categories = cls.objects.filter(category__icontains = search_term).all()

        try:
            images = []
            for category in categories:
                images_found = category.image_set.all()
                for image in images_found:
                    images.append(image)
            return images
        except:
            return "No images found"

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
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    categories = models.ManyToManyField(Categories)

    @property
    def location_name(self):
        return self.location.location

    def save_image(self):
        """
        Saves image to database
        """
        self.save()

    def update_image(self, property, value):
        """
        Updates image properties
        """
        if property == "image":
            self.image = value
        if property == "name":
            self.name = value
        if property == "decription":
            self.description = value
        if property == "location":
            self.location = value

    def delete_image(self):
        """
        Removes image from database
        """
        self.delete()

    def add_category(self, category):
        """
        Adds new category to categories list
        """
        self.categories.add(category)
        
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__location__icontains = location)
        return images

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name