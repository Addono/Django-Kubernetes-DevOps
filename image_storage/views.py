from django.shortcuts import render

from image_storage.models import Image


def home(request):
    context = {
        'images': Image.objects.all(),
    }
    return render(request, 'image_storage/home.html', context)
