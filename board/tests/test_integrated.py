from urllib import response
from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from accounts.models import Employee
from ..models import Post

class TestBoard(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'test_user'
        self.password = 'test'
        user = Employee.objects.create_user(username=self.username, password=self.password)
        user.save()

        self.title = 'test_title'
        self.contents = 'test_contens'
        self.title_r = 'test_title_r'
        self.contents_r = 'test_contens_r'
        self.client.login(username=self.username, password=self.password)

    def tearDown(self):
        user = Employee.objects.all().first()
        user.delete()

    def test_post_create(self):
        response = self.client.post(reverse('board:post_create'), {'title':self.title, 'contents':self.contents})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('board:post_list'))

        p = Post.objects.first()
        u = Employee.objects.first()
        self.assertEqual(p.title, self.title)
        self.assertEqual(p.contents, self.contents)
        self.assertEqual(p.contributer, u.username)
        self.assertIsNotNone(p.pub_date)

    def test_post_detail(self):
        self.client.post(reverse('board:post_create'), {'title':self.title, 'contents':self.contents})
        response = self.client.get('/board/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.title)

        p = Post.objects.first()
        u = Employee.objects.first()
        response = self.client.get(reverse('board:post_detail', kwargs={'pk': p.pk}))
        self.assertContains(response, self.title)
        self.assertContains(response, self.contents)
        
    def test_post_edit(self):
        self.client.post(reverse('board:post_create'), {'title':self.title, 'contents':self.contents})

        p = Post.objects.first()
        u = Employee.objects.first()
        response = self.client.post(reverse('board:post_update', kwargs={'pk': p.pk}), {'title':self.title_r, 'contents':self.contents_r})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('board:post_detail', kwargs={'pk': p.pk}))

        response = self.client.get(reverse('board:post_list'))
        self.assertContains(response, self.title_r)

        response = self.client.get(reverse('board:post_detail', kwargs={'pk': p.pk}))
        self.assertContains(response, self.title_r)
        self.assertContains(response, self.contents_r)

    def test_post_delete(self):
        self.client.post(reverse('board:post_create'), {'title':self.title, 'contents':self.contents})
        self.assertEqual(Post.objects.all().count(), 1)
        
        p = Post.objects.first()
        response = self.client.post(reverse('board:post_delete', kwargs={'pk': p.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('board:post_list'))
        self.assertEqual(Post.objects.all().count(), 0)








