from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
    # pylint: disable=no-member 
    queryset = TaggedItem.objects.get_tags_for(Product,1)

    return render(request, 'hello.html', {'name': 'Wasee', 'result':list(queryset)})