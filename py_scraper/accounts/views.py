from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from scraper.forms import ScrapeForm
from scraper.tasks import scrap
from scraper.views import the_scraper
from django.core.paginator import Paginator

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


@login_required
def dashboard(request):
    user = request.user
    scraped_pages = user.scraped_pages.all()
    if request.method == 'POST':
        form = ScrapeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            the_scraper(url, user.id)
            return redirect('dashboard')
    else:
        form = ScrapeForm()
    pages_paginator = Paginator(scraped_pages, 10)
    page_num = request.GET.get('page', 1)
    page = pages_paginator.get_page(page_num)
    context = {
        'user': user,
        'form': form,
        'scraped_pages': scraped_pages,
        'count' : pages_paginator.count,
        'page' : page
    }
    return render(request, 'dashboard.html', context)