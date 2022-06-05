from django.shortcuts import render
from django.http import HttpResponse

from insta.models import Image

# Create your views here.
def home(request):
    posts = Image.objects.all()

    return render(request, 'home.html', {'posts': posts})