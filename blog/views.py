from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def create_post(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            image=request.FILES.get('image'),
            author=request.user
        )
        return redirect('home')

    return render(request, 'create.html')


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']

        if 'image' in request.FILES:
            post.image = request.FILES['image']

        post.save()
        return redirect('home')

    return render(request, 'edit.html', {'post': post})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    post.delete()
    return redirect('home')


def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')