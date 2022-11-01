from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import PostModel
from .forms import UploadcontentForm, UploadfileForm, UploadphotoForm
# Create your views here.


def viaindex(request):
    return render(request, 'via/index.html')


def index(request):
    if request.method == 'POST':
        form1 = UploadcontentForm(request.POST)
        form2 = UploadphotoForm(request.POST or None, request.FILES)
        form3 = UploadfileForm(request.POST or None, request.FILES)
        if form1.is_valid() & form2.is_valid() & form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect('myapp-index')
    else:
        form1 = UploadcontentForm()
        form2 = UploadphotoForm()
        form3 = UploadfileForm()
    return render(request, 'myapp/index.html', {'form1': form1, 'form2': form2, 'form3': form3})
