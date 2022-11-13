from socket import fromshare
from django import forms
from .models import PostModel


class UploadcontentForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'image', 'data', 'metadata']


class EditcontentForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'image', 'data', 'metadata']

# class UploadphotoForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = ['image']


# class UploadfileForm(forms.ModelForm):
#     class Meta:
#         model = File
#         fields = ['metadata']
