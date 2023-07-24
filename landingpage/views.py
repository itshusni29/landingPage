from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost


def landing_page(request):
    return render(request, 'landigPage/index.html')

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'landigPage/create_blog_post.html', {'form': form})

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'landigPage/blog_list.html', {'blog_posts': blog_posts})
