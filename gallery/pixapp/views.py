from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images
import datetime as dt

# # Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to PixWall')

def welcome(request):
    return render(request, 'welcome.html')

def all_images(request):
    images = Images.get_images()
    return render(request, 'all_images.html', {"images": images})


def single_photo(request, photo_id):
    photo = Images.objects.get(id=photo_id)
    return render(request, 'single_image.html', {'photo':photo})
