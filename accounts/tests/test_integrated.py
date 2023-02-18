from urllib import response
from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Employee

class TestAccounts(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'test_user'
        self.password = 'test'
        user = Employee.objects.create_user(username=self.username, password=self.password)
        user.save()

    def tearDown(self):
        user = Employee.objects.all().first()
        user.delete()

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertContains(response, 'ユーザー名')
        self.assertContains(response, 'パスワード')
        self.assertEqual(response.status_code, 200)

    def test_login_page_another_url(self):
        response = self.client.get('/')
        self.assertContains(response, 'ユーザー名')
        self.assertContains(response, 'パスワード')
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        response = self.client.post('/login/', {'username':self.username,'password':self.password})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(settings.LOGIN_REDIRECT_URL))

    def test_logout_success(self):
        response = self.client.post('/login/', {'username':self.username,'password':self.password})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(settings.LOGIN_REDIRECT_URL))
        
        response = self.client.post('/logout/')
        self.assertContains(response, 'Logoutしました')
        
        response = self.client.get('/board/')
        self.assertEqual(response.status_code, 302)
