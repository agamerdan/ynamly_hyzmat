from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from .forms import LoginForm
from django.contrib import messages
from .models import Profile

def giris(request):
    
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is None:
                messages.warning(request,"Ulgamda Açılan Hasabynyz Yok")
                return render(request,'giris.html',context)
            messages.success(request,"Ulgama Girmeyi Başardynyz")
            login(request,user)
            return redirect('index')
    return render(request, 'giris.html',context)
  



def yazil(request):
    if request.method=="POST" or request.method=="FILES":
        bilgiler=request.POST
        ad=bilgiler.get("fname")
        soyad=bilgiler.get("lname")
        uname=bilgiler.get("uname")
        pasword=bilgiler.get("psw")
        pasword_confirim=bilgiler.get("psw_confirim")
        avatar=request.FILES.get("filename")
        if avatar:
            print("yüklendi")
        
        if len(ad)<3 or len(soyad)<3 or len(uname)<3 or len(pasword)<3:
            messages.error(request, "İn az 3 harp girip bilersiniz")
            return redirect("yazil")
        if pasword!=pasword_confirim:
            messages.warning(request, "Şifre bile şifre tekrarı eşit değil")
            return redirect("yazil")
        user, created=User.objects.get_or_create(username=uname)
        if created:
            user.first_name=ad
            user.last_name=soyad
            user.username=uname
            
            profile, profil_created=Profile.objects.get_or_create(user=user)
            profile.avatar=avatar
            user.set_password(pasword)
            user.save()
            profile.save()
            messages.success(request, "Kullanıcı oluşturuldu")
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, "Bu Hesap adı bln giriş yapıldı, Başka hesap açyn ")
            return redirect("yazil.html")
    return render (request, "yazil.html")
        
   

def cikis(request):
    messages.info(request, "Ulgamdan Çıkdınız")
    logout(request)
    return redirect("index")
    






