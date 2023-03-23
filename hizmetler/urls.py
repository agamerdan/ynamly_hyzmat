from django.contrib import admin
from django.urls import path
from . import views
#http://127.0.0.1:8000/
app_name="hizmet"

urlpatterns = [
    
    
    path('hizmetlerim/', views.hizmetlerim, name="hizmetlerim"),
    path('hizmet_ekle/', views.hizmet_ekle, name="hizmet_ekle"),
    path('yorum/<int:id>', views.yorum, name="yorum"),
    path('hizmetlerim/detay/<int:id>', views.detay, name="detay"),
    path('hizmetlerim/duzelt/<int:id>', views.duzelt, name="duzelt"),
    path('hizmetlerim/poz/<int:id>', views.poz, name="poz"),
    path('hizmetler/', views.hizmetler, name="hizmetler"),
    
   
]