from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
   
    
    class Meta:
        model = Article
        fields = ("telefon","title","fiyatbilgisi","content","hizmet_img")
        

