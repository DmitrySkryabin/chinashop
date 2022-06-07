from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'shop/index.html', context)