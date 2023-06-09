# Generated by Django 4.1.4 on 2023-02-16 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hizmetler', '0002_article_hizmet_img_alter_article_adsoyad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Yorumlayan')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Yorum içerigi')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='hizmetler.article', verbose_name='Huzmat')),
            ],
        ),
    ]
