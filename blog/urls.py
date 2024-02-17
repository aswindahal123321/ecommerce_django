from django.urls import path, include
from blog import views

urlpatterns = [
       path('', views.index, name="blogHome"),
       path('blogpost/<int:blog_id>', views.blogpost, name="blogPost"),
       path('search/', views.search, name="search"),
       path('signup/', views.handleSignUp, name="handleSignUp"),
       path('login/', views.handleLogin, name="handleLogin"),
       path('logout/', views.handleLogout, name="handleLogout"),
]
