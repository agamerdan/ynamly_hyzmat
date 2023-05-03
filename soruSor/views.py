from django.shortcuts import render
from django.contrib import messages
from .models import Sorusor

def soruSor(request):
    sorular=Sorusor.objects.all()
    context={
        "sorular": sorular
    }
    sorusor=Sorusor()
    if request.method=='POST':
        print("çalıştı")
        title=request.POST.get('soru_title')
        content=request.POST.get('soru_content')
        sorusor.title=title
        sorusor.content=content
        sorusor.author=request.user
        sorusor.adSoyad=request.user.first_name +" "+ request.user.last_name
        if request.user.profile.avatar:
           sorusor.soran_avatar=request.user.profile.avatar
         
        messages.success(request, "Soragynyz Yayynlandy")
        sorusor.save()
    
    return render(request, "sorusor.html", context)
