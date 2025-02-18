from django.shortcuts import render
from django.db.models import Value, F, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Order, Customer

def say_hello(request):
    # pylint: disable=no-member 
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8 , output_field= DecimalField())
    queryset = Product.objects.annotate(
        discounted_price= discounted_price
    )
    return render(request, 'hello.html', {'name': 'Wasee', 'result':list(queryset)})