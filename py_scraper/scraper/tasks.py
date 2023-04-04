from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen
from .models import ScrapedPage, ScrapedLink
from django.contrib.auth.models import User

@shared_task
def scrap(url, user_id):
    try:
        html = urlopen(url).read()
        
        soup = BeautifulSoup(html, 'html.parser')

        scraped_page = ScrapedPage.objects.create(user=User.objects.get(id=user_id), url=url, name=soup.title.string)

        links = soup.find_all('a')

        for link in links:
            url = link.get('href')
            name = link.string if link.string else url
            if url:
                ScrapedLink.objects.create(page=scraped_page, url=url, name=name)
        
        scraped_page.status = 'completed'
        scraped_page.save()
    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")
