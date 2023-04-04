from django.test import TestCase
from scraper.tasks import scrap

class CeleryTestCase(TestCase):
    
    def test_add_task(self):
        result = scrap.delay("http://google.com")
        self.assertEqual(result.get(), "http://google.com")
