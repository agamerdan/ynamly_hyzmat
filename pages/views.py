from django.shortcuts import render,get_object_or_404
from hizmetler.models import Article






def index(request):
    query=request.GET.get('keyword')
    article=Article.objects.filter(title="Kimlik")
    if(query):
        arananlar=Article.objects.filter(title=query)
        return render(request, 'hizmetler.html',{"arananlar":arananlar})
    return render(request, 'index.html', {"article":article})

def about(request):
    return render(request, 'about.html')








