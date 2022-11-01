# Generated by Django 4.0.6 on 2022-10-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_file_file_remove_photo_image_postmodel_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='metadata',
        ),
        migrations.AddField(
            model_name='file',
            name='metadata',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
