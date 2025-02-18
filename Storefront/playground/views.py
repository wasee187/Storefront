from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from store.models import Product, Order, Customer

def say_hello(request):
    # pylint: disable=no-member 
    queryset = Customer.objects.annotate(
        orders_count = Count('order')
    )
    return render(request, 'hello.html', {'name': 'Wasee', 'result':list(queryset)})