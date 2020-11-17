from django.shortcuts import render, redirect
from .models import *
from django.http import Http404


# Create your views here.
def index(request):
    images = Image.objects.all()
    ctx = {"images":images}
    return render(request, "gallery/index.html", ctx)