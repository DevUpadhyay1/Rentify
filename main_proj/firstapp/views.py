from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from table.models import *

# Create your views here.
def Index(request):
    return render(request,'Index.html')

def rent(request):
    return render(request,'rent.html')

def categories(request):
    return render(request,'categories.html')

def Index(request):
    image_paths = [
        'images/banglow.png',
        'images/CarRental.png',
        'images/Furniturerental.png',
        # Add other image paths as needed
    ]
    return render(request, 'Index.html', {'image_paths': image_paths})

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories":categories
    }

    return render(request, 'categories.html',context)