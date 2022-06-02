from django.shortcuts import render, HttpResponse
from .models import Post

def home(request):
    return HttpResponse("Hello Viewer we are in Blog views.py")

def blogHome(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context = {'allPosts': allPosts}
    return render(request,'blog/bloghome.html',context)

def Blogpost(request,slug):
    post = Post.objects.filter(slug =slug)[0]
    context = {'post':post}
    return render(request,'blog/blogpost.html',context)

# Create your views here.
