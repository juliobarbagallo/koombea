from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ScrapedPage(models.Model):
    STATUS_CHOICES = {
        'in_progress': 'In Progress',
        'completed': 'Completed',
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scraped_pages')
    url = models.URLField(unique=False)
    name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=list(STATUS_CHOICES.items()), default='in_progress')

    def __str__(self):
        return self.name or self.url

    @property
    def link_count(self):
        return self.links.count()

class ScrapedLink(models.Model):
    page = models.ForeignKey(ScrapedPage, on_delete=models.CASCADE, related_name='links')
    url = models.URLField()
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name or self.url
