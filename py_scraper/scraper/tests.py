from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase
from django.urls import reverse_lazy

from scraper.models import ScrapedLink, ScrapedPage


from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase

from scraper.models import ScrapedLink, ScrapedPage

SCRAPED_PAGE_DATA = {
    "user": {
        "username": "koombeauser",
        "password": "testpassword"
    },
    "url": "https://koombea.com",
    "name": "You App Development Partner"
}

SCRAPED_LINK_DATA = {
    "page": {
        "url": "https://koombea.com",
        "name": "You App Development Partner"
    },
    "url": "https://koombea.com/link1",
    "name": "Link 1"
}
class ScraperTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            **SCRAPED_PAGE_DATA["user"]
        )

        self.scraped_page = ScrapedPage.objects.create(
            user=self.user,
            url=SCRAPED_PAGE_DATA["url"],
            name=SCRAPED_PAGE_DATA["name"],
            status="completed",
        )

        self.scraped_link1 = ScrapedLink.objects.create(
            page=self.scraped_page,
            url=SCRAPED_LINK_DATA["url"],
            name=SCRAPED_LINK_DATA["name"]
        )
        self.scraped_link2 = ScrapedLink.objects.create(
            page=self.scraped_page,
            url="http://koombea.com/page2",
            name="Page 2"
        )
        self.scraped_link3 = ScrapedLink.objects.create(
            page=self.scraped_page,
            url="http://koombea.com/page3",
            name="Page 3"
        )

    def test_scraped_page_details_view(self):
        scraped_page = ScrapedPage.objects.create(
            user=self.user, url="http://koombea.com", name="You App Development Partner"
        )

        for i in range(20):
            ScrapedLink.objects.create(
                page=scraped_page, url=f"http://koombea.com/link{i}", name=f"Link {i}"
            )

        response = self.client.get(
            reverse("scraped_page_details", kwargs={"scraped_page_pk": scraped_page.pk})
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["scraped_page"], scraped_page)

        self.assertEqual(response.context["page"].number, 1)

        self.assertEqual(response.context["count"], 20)


class ScrapedPageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            **SCRAPED_PAGE_DATA["user"]
        )
        cls.scraped_page = ScrapedPage.objects.create(
            user=cls.user,
            url=SCRAPED_PAGE_DATA["url"],
            name=SCRAPED_PAGE_DATA["name"]
        )

    def test_model_fields(self):
        self.assertEqual(str(self.scraped_page.user), "koombeauser")
        self.assertEqual(self.scraped_page.url, "https://koombea.com")
        self.assertEqual(self.scraped_page.name, "You App Development Partner")
        self.assertEqual(self.scraped_page.status, "in_progress")

    def test_link_count_property(self):
        scraped_link1 = ScrapedLink.objects.create(
            page=self.scraped_page, url="https://koombea.com/link1", name="Link 1"
        )
        scraped_link2 = ScrapedLink.objects.create(
            page=self.scraped_page, url="https://koombea.com/link2", name="Link 2"
        )
        self.assertEqual(self.scraped_page.link_count, 2)

class ScrapedLinkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            **SCRAPED_PAGE_DATA["user"]
        )
        cls.scraped_page = ScrapedPage.objects.create(
            user=cls.user,
            url=SCRAPED_PAGE_DATA["url"],
            name=SCRAPED_PAGE_DATA["name"]
        )
        cls.scraped_link = ScrapedLink.objects.create(
            page=cls.scraped_page,
            url=SCRAPED_LINK_DATA["url"],
            name=SCRAPED_LINK_DATA["name"]
        )

    def test_model_fields_links(self):
        self.assertEqual(str(self.scraped_link.page), "You App Development Partner")
        self.assertEqual(self.scraped_link.url, "https://koombea.com/link1")
        self.assertEqual(self.scraped_link.name, "Link 1")