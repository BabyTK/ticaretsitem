# Generated by Django 3.1 on 2021-01-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210110_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Kategori Fotoğrafı'),
        ),
    ]
