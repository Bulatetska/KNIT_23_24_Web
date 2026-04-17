from django.urls import path

from .views import add_comment, post_create, post_detail, post_list

app_name = "blog"

urlpatterns = [
    path("", post_list, name="post_list"),
    path("new/", post_create, name="post_create"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
    path("post/<int:post_id>/comment/", add_comment, name="add_comment"),
]
