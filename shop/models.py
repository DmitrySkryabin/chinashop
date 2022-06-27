from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


PaymentMethod = (
    ('online', 'онлайн'),
    ('card', 'картой при получении'),
    ('cash','наличкой при получении')
)


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self',on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']


class Attribute(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model): 
    name = models.CharField(max_length=200)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    barcode = models.BigIntegerField()
    description = models.TextField()
    price = models.FloatField()
    count_of_buy = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return str(self.product) + '-' + str(self.attribute) + ':' + self.value


class Address(models.Model):
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    building = models.CharField(max_length=20)
    floor = models.CharField(max_length=20 ,null=True, blank=True)
    apartment = models.CharField(max_length=20, null=True, blank=True)
    entrance = models.CharField(max_length=20, null=True, blank=True)
    intercom_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.district + self.city + self.street + self.building


class Order(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=PaymentMethod)
    total_cost = models.FloatField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + str(self.customer) 


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

