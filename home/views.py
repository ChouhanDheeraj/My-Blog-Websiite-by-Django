from django.db.models import query
from django.db.models.query_utils import PathInfo
from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from Blog.models import Post
def home(request):
    return render(request,'home/home.html')
    #return HttpResponse("Hello Viewer this is home")
def contact(request):
    
    if request.method == 'POST':
        name = request.POST['Name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['Content']
       
        if len(name)<2 or len(email)<6 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please fill valid information !!')
        else:
            contact = Contact(name = name,phone= phone,email= email,content= content)
            contact.save()
            messages.success(request, 'Your data has been submited sucessfully')
    return render(request,'home/contact.html')
def about(request):
   return render(request,'home/about.html')

def search(request):
    
    query = request.GET['query']
    if len(query)>50:
        allPosts= Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)

    if allPosts.count() == 0:
        messages.warning(request,"No search result found; Please make sure your query is valid")
    parms = {'allPosts': allPosts , 'query':query}
    return render(request,'home/search.html',parms)
    #return HttpResponse("Helo you are in search")
# Create your views here.
