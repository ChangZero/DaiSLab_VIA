from distutils.command.upload import upload
from email.mime import image
from turtle import title
from unittest.util import _MAX_LENGTH
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


def images_directory_path(instance, filename):

    now = datetime.datetime.now()

    path = "images/{username}/{year}/{month}/{filename}".format(
        year=now.year,
        month=now.month,
        username=instance.user.username,
        filename=filename,
    )
    return path


def datafiles_directory_path(instance, filename):

    now = datetime.datetime.now()

    path = "datafiless/{username}/{year}/{month}/{filename}".format(
        year=now.year,
        month=now.month,
        username=instance.user.username,
        filename=filename,
    )
    return path


def metadatafiles_directory_path(instance, filename):

    now = datetime.datetime.now()

    path = "metadatafiles/{username}/{year}/{month}/{filename}".format(
        year=now.year,
        month=now.month,
        username=instance.user.username,
        filename=filename,
    )
    return path


class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(
        upload_to=images_directory_path, validators=[FileExtensionValidator(['png', 'jpg'])], null=True, blank=True)

    data = models.FileField(
        upload_to=datafiles_directory_path, validators=[FileExtensionValidator(['csv', 'json', 'zip'])], null=True, blank=True)

    metadata = models.FileField(
        upload_to=metadatafiles_directory_path, validators=[
            FileExtensionValidator(['csv', 'json', 'zip'])], null=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):  # PostModel의 title을 admin에 넘겨주기 위해서 만듬
        return self.title
