from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Sorusor(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    soran_avatar=models.ImageField(blank=True, null=True)
    adSoyad=models.CharField(max_length=50, verbose_name="Ad we Familyanyz")
    title=models.CharField(max_length=50,verbose_name="Sory Temasy")
    content=models.TextField(verbose_name="Soru İçerigi")
    soru_image=models.FileField(blank=True, null=True)
    tarih=models.DateTimeField(auto_now_add=True)
    like=models.IntegerField(default=0, blank=True, null=True)
    likes=models.CharField(max_length=50, blank=True, null=True)
    cevap_sayi=models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.title

class Cevaplar(models.Model):
    soru=models.ForeignKey(Sorusor, on_delete=models.CASCADE, verbose_name="cevap", related_name="cevap")
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="cevap_user",blank=True,null=True)
    adSoyad=models.CharField(max_length=50)
    cevap_content=models.TextField(verbose_name="Cevap icerigi", default="+1")
    cevap_avatar=models.ImageField(blank=True, null=True)
    cevap_tarih=models.DateTimeField(auto_now_add=True)
    
class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    sorular=models.ForeignKey(Sorusor, on_delete=models.CASCADE, related_name="soru_like")
    like_resim=models.ImageField(default="resim/kalp.png")

    