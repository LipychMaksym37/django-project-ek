from django.contrib import admin
from .models import Seller, Category, Product


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'updated_at')

    from .models import Seller, Category, Product, CartItem, Subscriber, Rating

    admin.site.register(CartItem)
    admin.site.register(Subscriber)
    admin.site.register(Rating)