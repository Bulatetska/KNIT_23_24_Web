from django.test import TestCase
from django.urls import reverse

from .models import Comment, Post


class BlogViewsTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Перший пост",
            content="Текст першого поста",
            author_name="Міша",
        )

    def test_post_list_page_loads(self):
        response = self.client.get(reverse("blog:post_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Перший пост")

    def test_create_post(self):
        response = self.client.post(
            reverse("blog:post_create"),
            {
                "title": "Новий пост",
                "content": "Новий текст",
                "author_name": "Автор",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="Новий пост").exists())

    def test_post_detail_page_loads(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Текст першого поста")

    def test_add_comment(self):
        response = self.client.post(
            reverse("blog:add_comment", args=[self.post.id]),
            {
                "author_name": "Коментатор",
                "content": "Чудовий пост",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(post=self.post, author_name="Коментатор").exists())
