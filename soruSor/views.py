from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.contrib import messages
from .models import Sorusor
from .models import Cevaplar, Like
from django.core.paginator import Paginator

def soruSor(request):
    
    sorusor=Sorusor()
    if request.method=='POST' or request.method=="FILES":
        if request.user.is_authenticated:
            title=request.POST.get('soru_title')
            content=request.POST.get('soru_content')
            soru_image=request.POST.get('soru_image')
            sorusor.title=title
            sorusor.content=content
            sorusor.soru_image=soru_image
            sorusor.author=request.user
            sorusor.adSoyad=request.user.first_name +" "+ request.user.last_name
            if request.user.profile.avatar:
               sorusor.soran_avatar=request.user.profile.avatar
            
            messages.success(request, "Soragynyz Yayynlandy")
            sorusor.save()
        else:
            messages.error(request, "Sorag Sorap bilmeginiz üçün giriş yapmalysynyz")
            return redirect('giris')
    get_sorular=Sorusor.objects.all()
    paginator = Paginator(get_sorular, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    sorular = paginator.get_page(page_number)
    
    context={
        "sorular": sorular
    }
    
    return render(request, "sorusor.html", context)

def soru_detay(request,id):
    cevabim=False
    sorular=Sorusor.objects.filter(id=id).first()
    cevaplar=sorular.cevap.all()
    likes=sorular.likes
    if likes==request.user.username:
        like_status=True
    else:
        like_status=False
    content={
        "sorular":sorular,
        "cevaplar":cevaplar,
        "like_status":like_status,
        "cevabim":cevabim,
    }
    
    return render(request, "soru_detay.html",content)

def cevap(request, id):
    soru=get_object_or_404(Sorusor, id=id)
    if request.method=="POST":
        if request.user.is_authenticated:
            cevap_sayi=soru.cevap_sayi
            cevap_content=request.POST.get('cevap_content')
            cevap_content=cevap_content
            adSoyad=request.user.first_name +" "+ request.user.last_name
            cevap_ekle=Cevaplar(cevap_content=cevap_content, adSoyad=adSoyad)
            if request.user.profile.avatar:
                cevap_ekle.cevap_avatar=request.user.profile.avatar
            cevap_ekle.soru=soru
            cevap_sayi+=1
            soru.cevap_sayi=cevap_sayi
            soru.save()
            cevap_ekle.save()
        else:
            messages.warning(request, "Cevaplamak için giriş yapınız")
            return redirect('giris')
    return redirect(reverse('soru:soru_detay', kwargs={"id":id}))

def sorular_likes(request, id):
     if request.user.is_authenticated:
         user=request.user
         soru=Sorusor.objects.get(id=id)
         current_likes=soru.like
         likes=soru.likes
         liked=Like.objects.filter(user=user,sorular=soru).count()
         if not liked:
           liked=Like.objects.create(user=user, sorular=soru)
           current_likes=current_likes+1
           likes=request.user.username
         else:
           liked=Like.objects.filter(user=user, sorular=soru).delete()
           current_likes=current_likes-1
           likes=""
         soru.likes=likes 
         soru.like=current_likes
         soru.save()
         
     else:
             messages.warning(request, "Begenebilmek için giriş yapmak gerekir")
             return redirect('giris')
    
     return redirect(reverse('soru:soru_detay',kwargs={"id":id}))