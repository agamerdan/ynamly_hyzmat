from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    adSoyad=models.CharField(max_length=50, verbose_name="Ad we Familyanyz")
    telefon = models.CharField(max_length=50, verbose_name="Telefon No")
    title=models.CharField(max_length=50,verbose_name="Hyzmatynyzyn Ady")
    fiyatbilgisi=models.CharField(max_length=50, verbose_name="Hyzmatynyzyn Bahasy")
    content=models.TextField(verbose_name="Hyzmatynyz Barada")
    hizmet_img=models.FileField(blank=True,null=True, verbose_name="Surat Yükle")
    tarih=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class CommentModel(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE, verbose_name="Hyzmat",related_name="comments")
    comment_author=models.CharField(max_length=50, verbose_name="Yorumlayan")
    comment_content=models.TextField(verbose_name="Yorum içerigi")
    comment_avatar=models.ImageField(blank=True , null=True )
    comment_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_author
    
