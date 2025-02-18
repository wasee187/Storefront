
from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, prodcut):
        if prodcut.inventory < 10 :
            return 'Low'
        return 'Ok'

@admin.register(models.Collection)
class CollectonAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10

#admin.site.register(models.Collection)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
