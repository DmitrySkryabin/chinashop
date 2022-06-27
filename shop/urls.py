from django.urls import path
from .views import index, index2, catalog_category, catalog_product

urlpatterns = [
    path('', index, name='home'),
    path('home2', index2, name='home2'),
    path('catalog_category/<category_id>', catalog_category, name="catalog_category"),
    path('catalog_product/<category_id>', catalog_product, name="catalog_product")
]

