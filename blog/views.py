# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Blog
from django.db.models import Q

# Create your views here.

def index(request):
    firstBlog = Blog.objects.filter(category = 'electronic')
    blogs = Blog.objects.all()
    print(blogs)
    context = {
        'blogs':blogs,      
    }
    return render(request, 'blog/index.html', context)

def search(request):
    query = request.GET.get('searchBlogs')
    if query:
        blogItems = Blog.objects.filter(Q(title__icontains = query) | Q(Heading__icontains = query) | Q(category__icontains = query) | Q(author__icontains = query))
    else:
        blogItems = []
        
    return render(request, 'blog/search-blog.html', {'query':query, 'blogItems': blogItems})


def blogpost(request, blog_id):
    singleBlog = Blog.objects.filter(blog_id = blog_id).first()
    singleBlog.views = singleBlog.views + 1
    singleBlog.save()
    blogs = Blog.objects.all()
    print(blogs)
    context = {
        'blogs':blogs, 
        'singleBlog': singleBlog       
    }
    return render(request, 'blog/blogpost.html', context)



def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST['fullname']
        contact = request.POST['contactnumber']
        email = request.POST['emailaddress']
        password1 = request.POST['newpassword1']
        password2 = request.POST['newpassword2']
        user = User.objects.create_user(username, email, password1)
        user.save()
        messages.success(request,"User Sign Up Success.")
        return redirect('blogHome')
    else:
        return HttpResponse("User not created")
        


def handleLogin(request):
    if request.method == 'POST':
        fullname = request.POST['fullnamelogin']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=fullname, password=loginpassword) 
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful.")  # Changed success message to reflect login
            return redirect('blogHome')
        else:
            messages.error(request, "Invalid Credentials.")
            return redirect('blogHome')

    return HttpResponse("404 Not Found")  # Moved inside the function for clarity


def handleLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successful")
        return redirect('blogHome')
    
    return HttpResponse("404 Not Found")

