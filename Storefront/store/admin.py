
from django.contrib import admin
from django.db.models import Count
from . import models


# Registering Product models from store app 

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, prodcut):
        if prodcut.inventory < 10 :
            return 'Low'
        return 'Ok' 


# Registering Order models from store app 

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at', 'customer']
    list_per_page = 10



# Registering Collection models from store app 

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    list_per_page = 10

    @admin.display(ordering ='products_count')
    def products_count(self, collection):
        return collection.products_count
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )




# Registering Customer models from store app 

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
