from django.contrib import admin

from main.models import CartItem, Category, DiscountCode, Product, ShoppingCart, ProductPriceHistory

admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(DiscountCode)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(ProductPriceHistory)
