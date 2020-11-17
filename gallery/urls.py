from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("search/", views.search_results, name="search_results"),
    path("location/<int:location_id>", views.location, name = "location"),
]
