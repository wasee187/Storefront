from django.shortcuts import render
from store.models import Product, Order

def say_hello(request):
    # pylint: disable=no-member
    #queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

    #exercise Get the last 5 orders with their customer and items (incl product) 

    #my_solution 

    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    return render(request, 'hello.html', {'name': 'Wasee', 'orders':list(queryset)})
