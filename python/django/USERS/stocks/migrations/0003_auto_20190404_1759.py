# Generated by Django 2.0.7 on 2019-04-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20190404_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
