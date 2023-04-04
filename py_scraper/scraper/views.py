from django.shortcuts import render
from .forms import ScrapeForm
from scraper.tasks import scrap

def the_scraper(url, user_id):
    scrap.delay(url, user_id)
