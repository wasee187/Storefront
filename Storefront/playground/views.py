from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem

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
    #queryset = Product.objects.filter(inventory=F('collection__id'))

    #queryset = Product.objects.order_by('title')
    #queryset = Product.objects.order_by('-title')
    #queryset = Product.objects.order_by('unit_price','-title')
    #queryset = Product.objects.order_by('unit_price','-title').reverse()
    #queryset = Product.objects.order_by('unit_price','-title')[0]
    #queryset = Product.objects.earliest('unit_price','-title')
    #queryset = Product.objects.latest('unit_price','-title')
    #queryset = Product.objects.all()[:5]
    #queryset = Product.objects.all()[5:10]

    #queryset = Product.objects.values('id', 'title')
    #queryset = Product.objects.values('id', 'title', 'collection__title') #inner join

    #queryset = Product.objects.values('id', 'title', 'orderitem__id').order_by('title')

    #Exercise: Select products that have been ordered and sort them by title.
    #my solution
    #queryset = OrderItem.objects.values('product_id', 'product__id', 'product__title').distinct().order_by('product__title')
    #instructor solution 
    queryset = Product.objects.filter(
        id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')
    return render(request, 'hello.html', {'name': 'Wasee', 'products':list(queryset)})
