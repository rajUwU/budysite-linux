# Generated by Django 3.0.7 on 2020-07-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budy', '0002_auto_20200720_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='userINFO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
