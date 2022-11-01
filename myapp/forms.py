from socket import fromshare
from django import forms
from .models import PostModel, Photo, File


class UploadcontentForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content']


class UploadphotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']


class UploadfileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['metadata']
