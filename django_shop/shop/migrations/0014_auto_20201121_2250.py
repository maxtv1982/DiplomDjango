# Generated by Django 3.1.2 on 2020-11-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20201121_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, verbose_name='итоговая стоимость'),
        ),
    ]
