# Generated by Django 2.1.1 on 2019-05-13 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190513_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerspurchases',
            name='purchase_day',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 13, 23, 43, 45, 190084), verbose_name='Purchase day'),
        ),
    ]
