# Generated by Django 4.1.4 on 2023-04-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hizmetler', '0013_remove_article_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
