from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from scraper.forms import ScrapedPageForm
from scraper.tasks import add


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
        form = ScrapedPageForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            add.delay(url)
            return redirect('dashboard')
    else:
        form = ScrapedPageForm()
    context = {
        'user': user,
        'form': form,
        'scraped_pages': scraped_pages
    }
    return render(request, 'dashboard.html', context)