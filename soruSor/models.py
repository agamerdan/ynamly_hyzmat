from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Sorusor(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    adSoyad=models.CharField(max_length=50, verbose_name="Ad we Familyanyz")
    title=models.CharField(max_length=50,verbose_name="Sory Temasy")
    content=models.TextField(verbose_name="Hyzmatynyz Barada")
    hizmet_img=models.FileField(blank=True,null=True, verbose_name="Surat Yükle")
    tarih=models.DateTimeField(auto_now_add=True)
    like=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

