# Generated by Django 5.0.4 on 2024-04-23 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ['sort'], 'verbose_name': 'Категорія страв', 'verbose_name_plural': 'Категорії страв'},
        ),
    ]
