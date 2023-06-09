# Generated by Django 4.1.4 on 2023-05-05 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soruSor', '0004_cevaplar_cevap_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorusor',
            name='likes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_resim', models.ImageField(default='resim/kalp.png', upload_to='')),
                ('sorular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soru_like', to='soruSor.sorusor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
