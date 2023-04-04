from django.core.paginator import Paginator

from scraper.tasks import scrap


def the_scraper(url, user_id):
    scrap.delay(url, user_id)


def scraped_page_details(request, scraped_page_pk):
    scraped_page = ScrapedPage.objects.get(pk=scraped_page_pk)
    scraped_links = scraped_page.links.all()
    link_paginator = Paginator(scraped_links, 10)
    page_num = request.GET.get("page", 1)
    page = link_paginator.get_page(page_num)
    context = {
        "scraped_page": scraped_page,
        "count": link_paginator.count,
        "page": page,
        "scraped_page_pk": scraped_page_pk,
    }
    return render(request, "scraped_page_details.html", context)
