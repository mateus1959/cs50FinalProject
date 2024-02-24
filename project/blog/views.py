from django.http import HttpResponse
from django.shortcuts import render
from .models import * 
import datetime

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {
        "posts": posts
    })
