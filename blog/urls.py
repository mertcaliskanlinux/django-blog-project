from django.urls import path
from blog import views
urlpatterns = [
    path("",views.index,name="home"),
    path("index/",views.index),
    path("blogs/",views.blogs,name="blogs"),
    path("categories/<slug:slug>",views.blogs_by_category,name="blogs_by_category"),
    path("blog/<slug:slug>/",views.blog_details,name="blog-details")
]
