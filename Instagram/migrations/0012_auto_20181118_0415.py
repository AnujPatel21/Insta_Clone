# Generated by Django 2.1.2 on 2018-11-18 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0011_auto_20181118_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='Documents/'),
        ),
    ]
