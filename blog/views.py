from django.shortcuts import render

from blog.models import Blog, Categories
from django.contrib.auth.decorators import login_required


def index(request):
    blogs = Blog.objects.filter(is_active=True,is_home=True)
    categories = Categories.objects.all()
    context = {
        'blogs':blogs,
        'categories':categories
    }
    return render (request,"blog/index.html",context)

@login_required(login_url='login')
def blogs(request):
    blog = Blog.objects.filter(is_active=True)
    categories = Categories.objects.all()

    context = {
        "blogs":blog,
        'categories':categories
    }
    return render(request,"blog/blogs.html",context)


@login_required(login_url='login')
def blog_details(request,slug):

    blog = Blog.objects.get(slug=slug)
    
    context = {
        'blog':blog
    }

    return render(request,"blog/blog-detail.html",context)

@login_required
def blogs_by_category(request,slug):
    blog = Categories.objects.get(slug=slug).blog_set.filter(is_active=True)
    # blog = Blog.objects.filter(is_active=True,categories__slug=slug) #buda category filter için olur
    categories = Categories.objects.all()

    context = {
        "blogs":blog,
        "categories":categories,
        "selected_category":slug #html'de active olarka kullandık menü tıklandıgında mavi olsun diye
    }
    return render(request,"blog/blogs.html",context)