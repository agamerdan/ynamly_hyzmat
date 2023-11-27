from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from .forms import LoginForm
from django.contrib import messages
from .models import Profile

def giris(request):
    if request.method=='POST':
       
        form=request.POST
        if form:
             username=form.get("usrnm")
             password=form.get("psw")
             user=authenticate(username=username,password=password)
             if user is None:
                 messages.warning(request,"Ulgamda Açılan Hasabynyz Yok")
                 return render(request,'users/giris.html')
             messages.success(request,"Ulgama Girmeyi Başardynyz")
             login(request,user)
             return redirect('index')
    return render(request, 'users/giris.html')
  



def Register(request):
    
    if request.method=="POST" or request.method=="FILES":
        
        bilgiler=request.POST
        ad=bilgiler.get("fname")
        soyad=bilgiler.get("lname")
        uname=bilgiler.get("uname")
        pasword=bilgiler.get("psw")
        pasword_confirim=bilgiler.get("psw_confirm")
        avatar=request.FILES.get("filename")
        print(request.FILES.get("filename"))   
        if len(ad)<3 or len(soyad)<3 or len(uname)<3 or len(pasword)<3:
            messages.error(request, "İn az 3 harp girip bilersiniz")
            return redirect("register")
        if pasword!=pasword_confirim:
            messages.warning(request, "Şifre bile şifre tekrarı eşit değil")
            return redirect("register")
        
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
            print("Bu Hesap adı bln giriş yapıldı, Başka hesap açyn ")
            return redirect("users/register.html")
    return render (request, "users/register.html")
        
   

def cikis(request):
    messages.info(request, "Ulgamdan Çıkdınız")
    logout(request)
    return redirect("index")
    






