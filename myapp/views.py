from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import PostModel
# Create your views here.


def viaindex(request):
    return render(request, 'via/index.html')


def index(request):
    return render(request, 'myapp/index.html')


def post(request):
    posts = PostModel.objects.all
