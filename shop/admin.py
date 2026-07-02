from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'price', 'category', 'created', 'available']
    list_filter = ['category', 'price', 'available', 'created']
    list_editable = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)