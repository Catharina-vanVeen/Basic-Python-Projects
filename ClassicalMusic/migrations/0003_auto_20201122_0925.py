# Generated by Django 2.2.5 on 2020-11-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassicalMusic', '0002_auto_20201119_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=260, verbose_name='Image URL'),
        ),
    ]
