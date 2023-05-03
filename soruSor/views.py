from django.shortcuts import render
from django.contrib import messages
from .models import Sorusor

def soruSor(request):
    sorusor=Sorusor()
    if request=='POST':
        title=request.post.get('soru_title')
        content=request.post.get('soru_content')
        sorusor.title=title
        sorusor.content=content
        sorusor.author=request.user
        sorusor.adSoyad=request.user.first_name +" "+ request.user.last_name
         
        messages.success(request, "Soragynyz Yayynlandy")
        sorusor.save()
    context={
        "sorusor":sorusor,
    }   
    return render(request, "sorusor.html", context)
