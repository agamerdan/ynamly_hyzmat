# Generated by Django 4.1.4 on 2023-04-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hizmetler', '0014_remove_article_likes_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]