# Generated by Django 5.0.4 on 2024-05-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
