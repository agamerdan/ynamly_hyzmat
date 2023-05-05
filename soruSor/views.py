from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.contrib import messages
from .models import Sorusor
from .models import Cevaplar
from django.core.paginator import Paginator

def soruSor(request):
    
    sorusor=Sorusor()
    if request.method=='POST':
        if request.user.is_authenticated:
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
    sorular=Sorusor.objects.filter(id=id).first()
    cevaplar=sorular.cevap.all()
    content={
        "sorular":sorular,
        "cevaplar":cevaplar,
    }
    
    return render(request, "soru_detay.html",content)

def cevap(request, id):
    soru=get_object_or_404(Sorusor, id=id)
    if(request.method=="POST"):
        if request.user.is_authenticated:
            cevap_ekle=Cevaplar()
            cevap_content=request.POST.get('cevap_content')
            cevap_ekle.cevap_content=cevap_content
            cevap_ekle.adSoyad=request.user.first_name +" "+ request.user.last_name
            if request.user.profile.avatar:
                cevap_ekle.cevap_avatar=request.user.profile.avatar
            cevap_ekle.soru=soru
            cevap_ekle.save()
        else:
            messages.warning(request, "Cevaplamak için giriş yapınız")
            return redirect('giris')
    return redirect(reverse('cevap', kwargs={"id":id}))