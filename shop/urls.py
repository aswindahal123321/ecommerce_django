from django.urls import path, include
from shop import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tracker', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('product-view/<int:myid>', views.ProductView, name='product-view'),
    path('checkout/', views.checkout, name='checkout'),
     
   ]
