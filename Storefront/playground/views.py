from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product

def say_hello(request):
    # pylint: disable=no-member
    #product = Product.objects.filter(pk=0).first() # result = none
    #exists = Product.objects.filter(pk=0).exists() # return boolean
    #try:
    #    product = Product.objects.get(pk=0)
    #except ObjectDoesNotExist:
     #   pass
    #queryset = Product.objects.filter(unit_price__gt = 20)
    #queryset = Product.objects.filter(unit_price__range = (20,30))
    #queryset = Product.objects.filter(collection__id=2)
    #queryset = Product.objects.filter(collection__id__range=(1,2,3))
    #queryset = Product.objects.filter(title__icontains='coffee')

    #queryset = Product.objects.filter(inventory__lt =10, unit_price__lt =20)
    #queryset = Product.objects.filter(Q(inventory__lt =10) | Q(unit_price__lt =20))
    #queryset = Product.objects.filter(Q(inventory__lt =10) & ~Q(unit_price__lt =20))
    #queryset = Product.objects.filter(inventory=F('unit_price'))
    queryset = Product.objects.filter(inventory=F('collection__id'))
    return render(request, 'hello.html', {'name': 'Wasee', 'products':list(queryset)})
