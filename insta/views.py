from django.shortcuts import render, redirect
from django.http import HttpResponse
from insta.models import Image
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

# Create your views here.
@login_required(login_url = 'accounts/login/')
def home(request):
    posts = Image.objects.all()

    return render(request, 'base-app/home.html', {'posts': posts})

def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = Image.search_username(search_term)
        message = f"{search_term}"

        return render(request, 'base-app/search.html', {"message": message, "posts": searched_users})

    else:
        message = "You have not searched for any user"
        return render(request, 'base-app/search.html', {"message": message})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})