from django.shortcuts import render

from store.models import Product, Order, OrderItem, Product, Customer,Collection

def say_hello(request):
    # pylint: disable=no-member    
    collection = Collection()
    collection.title = 'Vedio Games'
    collection.featured_product = Product(pk=1)
    collection.save()

    return render(request, 'hello.html', {'name': 'Wasee'})