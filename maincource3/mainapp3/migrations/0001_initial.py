# Generated by Django 4.2 on 2024-02-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk', models.TextField()),
                ('id_vk', models.TextField()),
                ('token_vk', models.TextField()),
            ],
        ),
    ]
