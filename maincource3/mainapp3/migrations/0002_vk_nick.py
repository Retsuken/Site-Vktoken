# Generated by Django 4.2 on 2024-02-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vk',
            name='nick',
            field=models.TextField(default='NickName'),
        ),
    ]
