from django.shortcuts import render
from django.http import HttpResponse

from insta.models import Image

# Create your views here.
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