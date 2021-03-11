from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name='Search'),
    path('productview/<int:myid>', views.productview, name="ProductView"),
    path('checkout/<int:id_b>', views.checkout, name="CheckOut"),
    path('signup/', views.handleSignup, name="handleSignup"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout")

]
