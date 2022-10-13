# Generated by Django 2.2.16 on 2022-10-04 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='promotions',
            name='description',
            field=models.TextField(null=True),
        ),
    ]