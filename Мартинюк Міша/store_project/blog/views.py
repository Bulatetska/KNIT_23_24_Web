from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Post


def post_list(request):
    query = request.GET.get("q", "").strip()
    posts = Post.objects.annotate(comment_count=Count("comments"))

    if query:
        posts = posts.filter(title__icontains=query)

    return render(request, "blog/post_list.html", {"posts": posts, "query": query})


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.prefetch_related("comments"), pk=post_id)
    comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comment_form": comment_form,
        },
    )


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog:post_detail", post_id=post.id)
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form})


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

    return redirect("blog:post_detail", post_id=post.id)
