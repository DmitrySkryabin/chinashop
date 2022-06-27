from unicodedata import category
from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def index(request):
    context = {
        'categories': Category.objects.all(),
        'category_root_count': 3
    }
    return render(request, 'shop/index.html', context)


def index2(requset):
    '''
    Вторая версия отображения меню
    '''
    cat = {}
    categories = Category.objects.all()
    count=0
    for category in categories:
        if category.level == 0:
            cat2 = {}
            for category2 in categories:
                if category2.level == 1 and category2.parent == category:
                    cat3 = []
                    for category3 in categories:
                        if category3.level == 2 and category3.parent == category2:
                            cat3.append(category3)
                            count += 1
                    cat2.update({
                        category2: cat3
                    })
            cat.update({
                category: cat2
            })

    print(cat)
    print(count)
    context = {
        'categories': cat,
    }

    return render(requset, 'shop/index2.html', context)


def catalog_category(request, category_id):
    categories = Category.objects.filter(parent__id=category_id).all()
    products = Product.objects.filter(category=category_id).all()
    
    if len(products) == 0:
        context = {
            'categories': categories,
        }

        return render(request, 'shop/catalog_category.html', context)
    else:
        context = {
            'products': products,
        }
        return render(request, 'shop/catalog_product.html', context)
    


