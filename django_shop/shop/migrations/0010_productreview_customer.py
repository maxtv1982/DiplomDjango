# Generated by Django 3.1.2 on 2020-11-18 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_productreview_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='покупатель'),
        ),
    ]
