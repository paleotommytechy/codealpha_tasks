from django.contrib import admin
from .models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','avaliable','created','updated']
    list_filter = ['avaliable','created','updated']
    list_editable = ['price','avaliable']
    prepopulated_fields = {'slug':('name',)}