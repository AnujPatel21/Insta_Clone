# Generated by Django 2.1.2 on 2018-11-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.FileField(upload_to='desktop/'),
        ),
    ]
