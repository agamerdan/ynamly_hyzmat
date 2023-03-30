from django.shortcuts import render,redirect, get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from . models import Article, CommentModel, Likes
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator



def hizmetler(request):
    get_articles = Article.objects.all()
    paginator = Paginator(get_articles, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'hizmetler.html', {'articles': articles})
    



def hizmetlerim(request):
    hizmetlerim=Article.objects.filter(author=request.user)
    context={
       "hizmetlerim":hizmetlerim, 
    }
    return render(request, 'hizmetlerim.html', context)

def hizmet_ekle(request):
    form=ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.adSoyad=request.user.first_name +" "+ request.user.last_name
        article.save()
        messages.success(request, "Hyzmatynyz hasaba alyndy we Yayynlandy")
        return redirect('hizmet:hizmetlerim')
   
    return render(request, 'hizmet_ekle.html',{"form":form})



def detay(request, id):
    hyzmat=Article.objects.filter(id=id).first()
    comment=hyzmat.comments.all()
    return render(request, "detay.html", {"hyzmat":hyzmat, "comment":comment})



def duzelt(request, id):
    hyzmat=Article.objects.filter(id=id).first()
    form=ArticleForm(request.POST or None, request.FILES or None, instance=hyzmat)
    if form.is_valid():
        hyzmat=form.save(commit=False)
        hyzmat.author=request.user
        hyzmat.save()
        return redirect('hizmet:hizmetlerim')
    return render(request, "duzelt.html",{"form":form})

def poz(request, id):
    hyzmat=Article.objects.filter(id=id)
    hyzmat.delete()
    messages.success(request, "Hyzmat silme işiniz tamamlandy")
    return redirect('hizmet:hizmetlerim')

def yorum(request, id):
    article=get_object_or_404(Article, id=id)
    
    if request.method=="POST":
        if request.user.is_authenticated:
            comment_author=request.user.first_name +" "+ request.user.last_name
            comment_content=request.POST.get("comment_content")
            newComment=CommentModel(comment_author=comment_author, comment_content=comment_content)
            newComment.article=article
            if request.user.profile.avatar:
              newComment.comment_avatar=request.user.profile.avatar
            newComment.save()
        else:
            messages.warning(request, "Yorum yapmak üçün giriş yapmanız gerek")
            return redirect('giris')
    return redirect(reverse("hizmet:detay",kwargs={"id":id}))

def artikle_likes(request, id):
    user=request.user
    article=Article.objects.get(id=id)
    current_likes=article.like
    liked=Likes.objects.filter(user=user,article=article).count()
    if not liked:
        liked=Likes.objects.create(user=user, article=article)
        current_likes=current_likes+1
    else:
        liked=Likes.objects.filter(user=user, article=article).delete()
        current_likes=current_likes-1
        
    article.like=current_likes
    print ("begenme", article.like)
    article.save()
    
    return redirect(reverse('hizmet:detay',kwargs={"id":id}))

