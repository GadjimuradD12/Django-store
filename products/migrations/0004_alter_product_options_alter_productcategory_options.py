# Generated by Django 4.2.2 on 2024-02-05 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_created_timestmp_basket_created_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
