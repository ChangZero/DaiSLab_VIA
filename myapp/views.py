from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import PostModel
from .forms import UploadcontentForm, EditcontentForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


def viaindex(request):
    return render(request, 'via/index.html')


def postupload(request):
    if request.method == 'POST':
        form = UploadcontentForm(request.POST or None, request.FILES)
        # form2 = UploadphotoForm(request.POST or None, request.FILES)
        # form3 = UploadfileForm(request.POST or None, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            # form2.save()
            # form3.save()
            form.save()
            return redirect('myapp-index')
    else:
        form = UploadcontentForm()

    return render(request, 'myapp/upload.html', {'form': form})


@login_required
def index(request):

    # 입력인자
    page = request.GET.get('page', 1)
    q = request.GET.get('q', "")
    # 조회
    logged_in_user = request.user
    posts = PostModel.objects.filter(user=logged_in_user)
    if q:
        posts = posts.filter(Q(title__icontains=q)).distinct()

    # 페이징처리
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)
    context = {'posts': page_obj, 'page': page, 'q': q}

    return render(request, 'myapp/index.html', context)


@login_required
def detail(request, post_id):
    post = PostModel.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'myapp/detail.html', context)


@login_required
def delete(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('myapp-index')
    context = {'post': post}
    return render(request, 'myapp/delete.html', context)


@login_required
def edit(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    if request.method == 'POST':
        form = EditcontentForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('myapp-detail', post_id=post_id)
    else:
        form = EditcontentForm(instance=post)

    context = {
        'form': form,
        # 'post': post,
    }
    return render(request, 'myapp/edit.html', context)
