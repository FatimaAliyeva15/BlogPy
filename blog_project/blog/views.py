from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView,DetailView
from django.urls import reverse_lazy
from .models import BlogPost
from .forms import BlogPostForms

def index(request):
    yazilar = BlogPost.objects.all()
    print(yazilar)
    return render(request, 'blog/index.html', {'yazilar': yazilar})



def post_create(request):
    if request.method == "POST":
        form = BlogPostForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
    else:
        form = BlogPostForms()

    return render(request, "blog/blog_form.html", {"form": form})
def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForms(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
    else:
        form = BlogPostForms(instance=post)
    return render(request, 'blog/blog_form.html', {'form':form})

def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("blog:index")
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})


