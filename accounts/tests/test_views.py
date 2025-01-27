from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


Cook = get_user_model()

class CookViewsTest(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(username="testcook", password="password123")

    def test_login_view(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_logout_view(self):
        self.client.login(username='testcook', password='password123')
        response = self.client.post(reverse("accounts:logout"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/logged_out.html")

    def test_cook_absolute_url(self):
        self.assertEqual(self.cook.get_absolute_url(), reverse("restaurant:cooks-detail", kwargs={"pk": self.cook.pk}))

