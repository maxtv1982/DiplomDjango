# Generated by Django 3.1.2 on 2020-11-29 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0015_auto_20201121_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='покупатель'),
        ),
        migrations.AlterField(
            model_name='productsfororder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_positions', to='shop.order', verbose_name='заказ'),
        ),
    ]
