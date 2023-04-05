from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from accounts.models import CustomUser
from scraper.models import ScrapedLink, ScrapedPage

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="koombeauser", email="koombeauser@koombea.com"
        )
        self.user.set_password("testpass")
        self.user.save()

    def test_username(self):
        user = CustomUser.objects.get(id=self.user.id)
        self.assertEqual(user.username, "koombeauser")

    def test_email(self):
        user = CustomUser.objects.get(id=self.user.id)
        self.assertEqual(user.email, "koombeauser@koombea.com")

    def test_is_active(self):
        user = CustomUser.objects.get(id=self.user.id)
        self.assertTrue(user.is_active)


class RegistrationViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def test_registration_response(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        response = self.client.post(
            reverse("register"),
            {
                "email": "mick@koombea.com",
                "username": "koombeauser",
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


class DashboardViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username="koombeauser", password="testpassword"
        )
        cls.client = Client()
        cls.client.login(username="koombeauser", password="testpassword")

    def test_dashboard_view_link_count_property(self):
        scraped_page = ScrapedPage.objects.create(
            user=self.user, url="http://koombea.com", name="You App Development Partner"
        )

        scraped_link1 = ScrapedLink.objects.create(
            page=scraped_page, url="http://koombea.com/link1", name="Link 1"
        )
        scraped_link2 = ScrapedLink.objects.create(
            page=scraped_page, url="http://koombea.com/link2", name="Link 2"
        )

        scraped_page = ScrapedPage.objects.get(id=scraped_page.id)

        self.assertEqual(scraped_page.link_count, 2)
