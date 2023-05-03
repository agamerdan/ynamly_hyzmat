from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.soruSor, name="soruSor"),
    
]