# Generated by Django 2.0.7 on 2018-11-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0016_settag_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageset',
            name='description',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
    ]