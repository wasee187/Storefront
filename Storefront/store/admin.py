
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models



# Registering Product models from store app 

class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory' 
    parameter_name = 'Inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset):  #filtering logic
        if self.value() == '<10': 
            return queryset.filter(inventory__lt =10)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, prodcut):
        if prodcut.inventory < 10 :
            return 'Low'
        return 'Ok' 

    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.' 
        )
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
    def products_count(self, collection): #defining products_count method
        url = (reverse('admin:store_product_changelist')  #url for product page with filtering 
                + '?'
                + urlencode({
                    'collection__id': str(collection.id) #getting collection id in string for filtering
                }))
        return format_html('<a href="{}">{}</a>',url, collection.products_count) #html code for the link
        
    def get_queryset(self, request): #ovveride get_queryset()
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )




# Registering Customer models from store app 

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith'] #searching option with case insensitive 

    @admin.display(ordering='orders_count') #ordering method based on orders_count
    def orders_count(self, customer): #defining orders_count method
        url = (reverse("admin:store_order_changelist") #generating url link with reverse method admin:app_model_pagename
                + '?' 
                + urlencode({
                    'customer__id' : str(customer.id) #using urlencode to get customer id for filtering
                }))
        return format_html('<a href="{}">{}</a>',url , customer.orders_count) #returning formated url with  customer's order count
        
    def get_queryset(self,request): #overriding queryset to get orders_count of each customer
        return super().get_queryset(request).annotate(
            orders_count = Count('order')
        )