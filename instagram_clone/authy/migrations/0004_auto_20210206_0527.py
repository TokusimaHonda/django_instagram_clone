# Generated by Django 3.1.5 on 2021-02-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0003_auto_20210204_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='user_directory_path', verbose_name='Picture'),
        ),
    ]
