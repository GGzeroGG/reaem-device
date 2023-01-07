# Generated by Django 3.1.dev20200410100027 on 2020-06-05 21:51

from django.db import migrations, models
import django.db.models.deletion
import apps.poster.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.BooleanField(default=False, verbose_name='Будет ли товар на слайдере?')),
                ('img', models.ImageField(help_text='700x200px', upload_to=apps.poster.models.poster_img_name, verbose_name='Изоброжение товара постере')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]
