from django.urls import path

from . import views

urlpatterns = [
    path(
        "scraped_page/<int:scraped_page_pk>",
        views.scraped_page_details,
        name="scraped_page_details",
    ),
]
