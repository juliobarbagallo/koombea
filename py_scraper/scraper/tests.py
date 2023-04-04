from django.test import TestCase
from scraper.tasks import add

class CeleryTestCase(TestCase):
    
    def test_add_task(self):
        result = add.delay(4, 4)
        self.assertEqual(result.get(), 8)
