from django.contrib import admin
from django.urls import path
from . import views
#http://127.0.0.1:8000/
urlpatterns = [
    
    path('giris/', views.giris, name="giris"),
    path('yazil/', views.yazil, name="yazil"),
    path('cikis/', views.cikis, name="cikis"),
    ]