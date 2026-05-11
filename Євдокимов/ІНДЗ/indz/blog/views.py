from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.db.models import Count, Q


def post_list(request):
    query = request.GET.get('q', '')
    posts = Post.objects.annotate(comment_count=Count('comments'))

    if query:
        posts = posts.filter(title__icontains=query)

    # Пагінація
    from django.core.paginator import Paginator
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'query': query,
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})


def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('post_detail', id=id)