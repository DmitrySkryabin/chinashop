from django.urls import path
from .views import index, index2, catalog_category

urlpatterns = [
    path('', index2, name='home2'),
    #path('home2', index2, name='home2'),
    path('catalog_category/<category_id>', catalog_category, name="catalog_category"),
]

