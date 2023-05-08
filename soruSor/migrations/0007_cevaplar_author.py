# Generated by Django 4.1.4 on 2023-05-06 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soruSor', '0006_sorusor_cevap_sayi'),
    ]

    operations = [
        migrations.AddField(
            model_name='cevaplar',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cevap_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
