# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, category
from .forms import commentForm

# Create your views here.
def home(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.ACTIVE)

    if request.method == 'POST':    
        form = commentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail')
    else:
        form=commentForm()    

    context = {
        'post': post,
        'form': form
    }  
    return render (request, 'blog/detail.html',context)