from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Registration(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField(null=True, blank=True)
    user_type = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50)
    status = models.CharField(default="pending", null=True, blank=True, max_length=50)

class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Product(models.Model):
    seller_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    image = models.FileField()
    category = models.CharField(max_length=50,  null=True, blank=True)
    def __str__(self):
            return self.product_name

class Wishlist(models.Model):
    user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
class Cart(models.Model):
    user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
class Order(models.Model):
    user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_status = models.CharField(default="booked", max_length=50)

class Review(models.Model):
    user_id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    image = models.FileField()


