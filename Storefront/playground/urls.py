from django.urls import path
from . import views

# URLConfiguartion
urlpatterns = [
    path('hello/', views.say_hello)
]
