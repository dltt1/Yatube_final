import shutil
import tempfile
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from http import HTTPStatus

from posts.models import Group, Post, Comment

User = get_user_model()
TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PostFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test')
        cls.group = Group.objects.create(
            title='test-group',
            slug='test-slug',
            description='test-description'
        )
        cls.form_data = {
            'text': 'test-post',
            'group': cls.group.id,
        }

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        self.guest = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(PostFormTests.user)

    def test_create_post(self):
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00'
            b'\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00'
            b'\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        form_data = {
            'text': 'test-text',
            'group': self.group.id,
            'author': self.user,
            'image': uploaded,
        }
        response = self.authorized_client.post(
            reverse('posts:post_create'),
            data=form_data,
            follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.text, 'test-text')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.group, PostFormTests.group)
        self.assertEqual(post.image, 'posts/small.gif')

    def test_edit_post(self):
        post = Post.objects.create(
            author=PostFormTests.user,
            text='test-post',
            group=PostFormTests.group,
        )
        new_post_text = 'new-text'
        new_group = Group.objects.create(
            title='new-test-group',
            slug='new-test-slug',
            description='new-test-description'
        )
        response = self.authorized_client.post(
            reverse('posts:post_edit', kwargs={'post_id': post.id}),
            data=PostFormTests.form_data,
            follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.authorized_client.post(
            reverse('posts:post_edit', kwargs={'post_id': post.id}),
            data={
                'text': new_post_text,
                'group': new_group.id,
            },
            follow=True,
        )
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.text, new_post_text)
        self.assertEqual(post.author, PostFormTests.user)
        self.assertEqual(post.group, new_group)
        old_group_response = self.authorized_client.get(
            reverse('posts:group_list', args=(PostFormTests.group.slug,))
        )
        self.assertEqual(
            old_group_response.context['page_obj'].paginator.count,
            0
        )

    def test_unauth_user_cant_publish_post(self):
        """Неавт. польз. не может сделать пост"""
        response = self.guest.get(
            reverse('posts:post_create'),
        )
        self.assertRedirects(
            response, reverse('users:login') + '?next=/create/'
        )

    def test_comment_create_form(self):
        """
        Проверка создания комментария через форму под постом
        """
        post = Post.objects.create(
            text='test-text',
            author=self.user,
            group=self.group
        )
        form_data = {
            'text': 'Comment'
        }
        response = self.authorized_client.post(
            reverse('posts:add_comment', kwargs={'post_id': post.id}),
            data=form_data,
            follow=True
        )
        self.assertRedirects(
            response,
            reverse('posts:post_detail', kwargs={
                'post_id': post.pk
            }))
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.text, 'Comment')
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.author, self.user)
