# Generated by Django 3.1 on 2020-08-25 10:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_auto_20200825_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='dateposted',
            field=models.DateField(default=datetime.datetime(2020, 8, 25, 10, 20, 2, 990406, tzinfo=utc)),
        ),
    ]
