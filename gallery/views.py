from django.shortcuts import render, redirect
from .models import *
from django.http import Http404

# Create your views here.
def index(request):
    locations = Location.objects.all()
    images = Image.objects.all()
    if len(images) > 0:
        ctx = {"images":images, "locations":locations}
        return render(request, "gallery/index.html", ctx)
    else:
        message = "No images uploaded."
        ctx = {"images":images, "message":message}
        return render(request, "gallery/index.html", ctx)

def search_results(request):
    locations = Location.objects.all()
    if "category" in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        images = Categories.search_images(search_term)
        message = f"Results for {search_term}. Found {len(images)} images."

        ctx = {"images":images, "message":message, "locations":locations}
        return render(request, "gallery/search_results.html", ctx)

    else:
        message = "You have not searched for any item."
        ctx = {"message":message, "locations":locations}
        return render(request, "gallery/search_results.html", ctx)

def location(request, location_id):
    try:
        locations = Location.objects.all()
        location = Location.objects.get(id = location_id).location
        images = Image.filter_by_location(location)

        if len(images) > 0:
            message = f"Images from {location}"
            ctx = {"images":images, "message":message, "locations":locations}
            return render(request, "gallery/search_results.html", ctx)
        else:
            message = f"No images from {location}"
            ctx = {"message":message, "locations":locations}
            return render(request, "gallery/search_results.html", ctx)
    except:
        raise Http404("Page does not exist.")

def all_locations(request):
    locations = Location.objects.all()
    if len(locations) > 0:
        ctx = {"locations":locations}
        return render(request, "gallery/all_locations.html", ctx)
    else:
        return redirect("home")