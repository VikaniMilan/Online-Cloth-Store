from django.db import models
from retailer.models import *
from index_app.models import *

class User_Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.IntegerField(default=0)

    class Meta:
        db_table = 'User_Order'

class Product(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Product/', default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Product'

class Order_Item(models.Model):
    Order_id = models.ForeignKey(User_Order, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Order_Item'

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'

class Wishlist(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Wishlist'