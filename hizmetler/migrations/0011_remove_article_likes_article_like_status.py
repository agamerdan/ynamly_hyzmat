# Generated by Django 4.1.4 on 2023-04-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hizmetler', '0010_article_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
        migrations.AddField(
            model_name='article',
            name='like_status',
            field=models.BooleanField(default=False),
        ),
    ]
