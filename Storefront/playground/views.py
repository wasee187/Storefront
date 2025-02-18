from django.shortcuts import render
from django.db import transaction
from store.models import Product, Order, OrderItem, Product, Customer,Collection

def say_hello(request):
    # pylint: disable=no-member  

    with transaction.atomic():  
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.quantity = 1
        item.unit_price = 10
        item.product_id = 1
        item.save()

    return render(request, 'hello.html', {'name': 'Wasee'})