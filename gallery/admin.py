from django.contrib import admin
from .models import *

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ("categories",)

# Register your models here.
admin.site.register(Image, ImageAdmin)
admin.site.register(Location)
admin.site.register(Categories)