
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Landing page / upload form
]
