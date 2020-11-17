from django.shortcuts import render, redirect
from .models import *
from django.http import Http404

# Create your views here.
def index(request):
    images = Image.objects.all()
    ctx = {"images":images}
    return render(request, "gallery/index.html", ctx)

def search_results(request):
    if "category" in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        images = Categories.search_images(search_term)
        message = f"Results for {search_term}. Found {len(images)} images."

        ctx = {"images":images, "message":message}
        return render(request, "gallery/search_results.html", ctx)

    else:
        message = "You have not searched for any item."
        ctx = {"message":message}
        return render(request, "gallery/search_results.html", ctx)