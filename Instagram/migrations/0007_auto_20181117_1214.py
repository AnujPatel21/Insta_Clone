# Generated by Django 2.1.2 on 2018-11-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0006_auto_20181117_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Documents/'),
        ),
    ]