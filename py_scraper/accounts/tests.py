from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import CustomUser


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="testuser", email="testuser@koombea.com"
        )
        self.user.set_password("testpass")
        self.user.save()

    def test_username(self):
        user = CustomUser.objects.get(id=self.user.id)
        self.assertEqual(user.username, "testuser")

    def test_email(self):
        user = CustomUser.objects.get(id=self.user.id)
        self.assertEqual(user.email, "testuser@koombea.com")

    def test_is_active(self):
        user = CustomUser.objects.get(id=self.user.id)
        self.assertTrue(user.is_active)


class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration_response(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        response = self.client.post(
            reverse("register"),
            {
                "email": "test@koombea.com",
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_unauthenticated_redirec_to_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(
            response, reverse("login") + "?next=" + reverse("dashboard")
        )
