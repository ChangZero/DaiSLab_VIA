from django.shortcuts import render, redirect
from myapp.models import PostModel
from .forms import UploadcontentForm
# Create your views here.


def viaindex(request):
    return render(request, 'via/index.html')


def postupload(request):
    if request.method == 'POST':
        form = UploadcontentForm(request.POST or None, request.FILES)
        # form2 = UploadphotoForm(request.POST or None, request.FILES)
        # form3 = UploadfileForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            # form2.save()
            # form3.save()
            return redirect('myapp-index')
    else:
        form = UploadcontentForm()

    return render(request, 'myapp/upload.html', {'form1': form})


def index(request):
    posts = PostModel.objects.all()
    context = {'posts': posts}
    return render(request, 'myapp/index.html', context)


def detail(request, post_id):
    post = PostModel.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'myapp/detail.html', context)
