# Generated by Django 3.2.8 on 2021-11-02 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_product_model_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category',
        ),
    ]