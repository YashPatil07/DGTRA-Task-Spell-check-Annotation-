# pdfap/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Landing page / upload form
    # path('annotated/', views.annotated_pdf, name='annotated_pdf'),  # Download link page
]
