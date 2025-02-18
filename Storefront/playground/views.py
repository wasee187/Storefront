from django.shortcuts import render
from store.models import Product, Order, OrderItem, Product, Customer,Collection

def say_hello(request):
    # pylint: disable=no-member    
    #collection = Collection.objects.get(pk=11)
    #collection.featured_product = None
    #collection.save()

    Collection.objects.filter(pk=11).update(featured_product=None)
    return render(request, 'hello.html', {'name': 'Wasee'})