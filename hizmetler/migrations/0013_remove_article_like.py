# Generated by Django 4.1.4 on 2023-04-08 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hizmetler', '0012_remove_article_like_status_article_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like',
        ),
    ]