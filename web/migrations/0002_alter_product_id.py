# Generated by Django 3.2.8 on 2021-10-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(default=9, primary_key=True, serialize=False),
        ),
    ]