from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase

from scraper.models import ScrapedLink, ScrapedPage


class ScraperTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        self.scraped_page = ScrapedPage.objects.create(
            user=self.user,
            url="http://example.com",
            name="Example",
            status="completed",
        )

        self.scraped_link1 = ScrapedLink.objects.create(
            page=self.scraped_page, url="http://example.com/page1", name="Page 1"
        )
        self.scraped_link2 = ScrapedLink.objects.create(
            page=self.scraped_page, url="http://example.com/page2", name="Page 2"
        )
        self.scraped_link3 = ScrapedLink.objects.create(
            page=self.scraped_page, url="http://example.com/page3", name="Page 3"
        )

    def test_scraped_page_details_view(self):
        scraped_page = ScrapedPage.objects.create(
            user=self.user, url="http://example.com", name="Example"
        )

        for i in range(20):
            ScrapedLink.objects.create(
                page=scraped_page, url=f"http://example.com/link{i}", name=f"Link {i}"
            )

        response = self.client.get(
            reverse("scraped_page_details", kwargs={"scraped_page_pk": scraped_page.pk})
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["scraped_page"], scraped_page)

        self.assertEqual(response.context["page"].number, 1)

        self.assertEqual(response.context["count"], 20)


class ScrapedPageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.scraped_page = ScrapedPage.objects.create(
            user=self.user, url="https://example.com", name="Example"
        )

    def test_model_fields(self):
        self.assertEqual(str(self.scraped_page.user), "testuser")
        self.assertEqual(self.scraped_page.url, "https://example.com")
        self.assertEqual(self.scraped_page.name, "Example")
        self.assertEqual(self.scraped_page.status, "in_progress")

    def test_link_count_property(self):
        scraped_link1 = ScrapedLink.objects.create(
            page=self.scraped_page, url="https://example.com/link1", name="Link 1"
        )
        scraped_link2 = ScrapedLink.objects.create(
            page=self.scraped_page, url="https://example.com/link2", name="Link 2"
        )
        self.assertEqual(self.scraped_page.link_count, 2)


class ScrapedLinkModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.scraped_page = ScrapedPage.objects.create(
            user=self.user, url="https://example.com", name="Example"
        )
        self.scraped_link = ScrapedLink.objects.create(
            page=self.scraped_page, url="https://example.com/link1", name="Link 1"
        )

    def test_model_fields_links(self):
        self.assertEqual(str(self.scraped_link.page), "Example")
        self.assertEqual(self.scraped_link.url, "https://example.com/link1")
        self.assertEqual(self.scraped_link.name, "Link 1")
