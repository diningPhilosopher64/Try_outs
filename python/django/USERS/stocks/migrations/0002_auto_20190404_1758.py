# Generated by Django 2.0.7 on 2019-04-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
