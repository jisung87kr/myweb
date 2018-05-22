from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Cate
from .forms import PostForm
from django.utils import timezone




# Create your views here.
def index(request):
    posts = Post.objects.all()
    cates = Cate.objects.all()
    return render(request, 'blog/index.html', {
    'posts' : posts,
    'cates' : cates
    })

def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_view.html', {'post' : post})

def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_view', pk=post.pk)
        else :
            return HttpResponse('잘못된 값이 들어왔습니다.')
    else :
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST' :
        form = PostForm(request.POST, request.FILES, instance=post);
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_view', pk=post.pk)
        else :
            return HttpResponse('잘못된 값이 들어왔습니다.')
    else :
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form' : form})
