from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>', views.product_detail) #for accepting only integer value for id in the URL
]
