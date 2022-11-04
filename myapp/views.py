from django.shortcuts import render, redirect
from myapp.models import PostModel
from .forms import UploadcontentForm
from django.core.paginator import Paginator

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

    # 입력인자
    page = request.GET.get('page', 1)

    # 조회
    posts = PostModel.objects.all()

    # 페이징처리
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)

    context = {'posts': page_obj}
    return render(request, 'myapp/index.html', context)


def detail(request, post_id):
    post = PostModel.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'myapp/detail.html', context)


def search(request):
    posts = PostModel.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        posts = posts.filter(title__icontains=q)
        return render(request, 'myapp/search.html', {'posts': posts, 'q': q})

    else:
        return render(request, 'myapp/search.html')
