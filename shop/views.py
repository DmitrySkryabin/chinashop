from django.shortcuts import render
from .models import Product, Category, CategoryRelationship

# Create your views here.


def index(request):

    cat = []
    categorys = Category.objects.all()
    category_relationship_parent = CategoryRelationship.objects.all().values_list('parent_category')
    category_relationship_child = CategoryRelationship.objects.all().values_list('child_category')
    for category in categorys:
        if category.id not in [item[0] for item in category_relationship_parent]:
            cat.append(category)


    contex = {
        'categorys': [item.id for item in categorys],
        'category_parent': [item[0] for item in category_relationship_parent],
        'category_child': [item[0] for item in category_relationship_child]
    }
    print(cat)

    return render(request, 'shop/index.html', contex)