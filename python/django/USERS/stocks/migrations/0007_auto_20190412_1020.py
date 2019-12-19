# Generated by Django 2.0.7 on 2019-04-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_auto_20190412_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='is_Downloaded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='company_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.TextField(blank=True, default='/', null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_data',
            field=models.TextField(blank=True, default='Temp'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]