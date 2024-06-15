from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    image_url = models.URLField(default="")
    depth = models.IntegerField(default=0)  # Ensures depth doesn't exceed 5

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category, related_name="products")
    images = ArrayField(models.URLField(), blank=True, null=True)
    videos = ArrayField(models.URLField(), blank=True, null=True)
    image_url = models.URLField(default="")
    view_count = models.IntegerField(default=0)  # Tracks views on the product

    def __str__(self):
        return self.name


class DiscountCode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount_percentage = models.IntegerField(null=True, blank=True)
    discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    max_discount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    products = models.ManyToManyField(Product, blank=True, related_name="discounts")
    categories = models.ManyToManyField(Category, blank=True, related_name="discounts")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="shopping_cart"
    )
    products = models.ManyToManyField(Product, through="CartItem")


class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
