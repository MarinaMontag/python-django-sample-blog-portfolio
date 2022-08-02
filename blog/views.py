from django.shortcuts import render
from blog.models import Post, Category, Comment
from blog.forms import CommentForm


def all_posts(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog/all_posts.html', {'posts': posts})


def category_posts(request, category):
    category_obj = Category.objects.get(name=category)
    posts = category_obj.posts.all().order_by('-created_on')
    return render(request, 'blog/category_posts.html', {'posts': posts, 'category': category})


def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    return render(request, 'blog/blog_details.html', {'post': post, 'comments': comments, 'form': form})