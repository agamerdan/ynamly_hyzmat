from django.urls import path
from . import views
app_name="soru"
urlpatterns = [
    
    path('', views.soruSor, name="soruSor"),
    path('soru_detay/<int:id>', views.soru_detay, name="soru_detay"),
    path('cevap/<int:id>', views.cevap, name="cevap"),
    path('sorular_likes/<int:id>', views.sorular_likes, name="sorular_likes"),
]