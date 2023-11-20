from django.shortcuts import render,redirect, get_object_or_404
from .forms import PostForm
from .models import More,Post


def all_mores(request):
    post =Post.objects.all()
    mores =More.objects.order_by('-date') [:3]
    return render(request, 'more/all_mores.html', {'mores':mores , 'post':post})


def detail(request, more_id):
    more = get_object_or_404(More, pk=more_id)
    return render(request, 'more/detail.html', {'more':more}) 




# from .models import Post

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('post_edit', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'more/post_detail.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'more/post_edit.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'more/post_edit.html', {'form': form})