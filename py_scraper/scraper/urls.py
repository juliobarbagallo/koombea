from django.urls import path
from . import views

urlpatterns = [
    path('scraped_page/<int:scraped_page_pk>', views.scraped_page_details, name='scraped_page_details'),
    # path('scraped_page/<int:page_number>/', views.scraped_page_details, name='scraped_page_details'),
    # path('scraper/scraped_page/<int:scraped_page_pk>/', views.scraped_page_details, name='scraped_page_details'),
    # path('scraped_page/<int:scraped_page_pk>/', views.scraped_page_details, name='scraped_page_details'),
]
