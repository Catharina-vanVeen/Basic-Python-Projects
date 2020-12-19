# Generated by Django 2.2.5 on 2020-11-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassicalMusic', '0003_auto_20201122_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=260, verbose_name='Cover art URL'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='order_number',
            field=models.IntegerField(verbose_name='#'),
        ),
    ]
