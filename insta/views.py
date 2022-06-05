from django.shortcuts import render
from django.http import HttpResponse

from insta.models import Image

# Create your views here.
def home(request):
    posts = Image.objects.all()

    return render(request, 'base-app/home.html', {'posts': posts})

def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_name = request.GET.get("name")
        searched_images = Image.search_image(search_name)
        message = f"{search_name}"

        return render(request, 'search.html', {"message": message, "posts": searched_images})

    else:
        message = "You have not searched for any post"
        return render(request, 'search.html', {"message": message})