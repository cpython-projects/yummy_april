# Generated by Django 5.0.4 on 2024-04-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('sort', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
