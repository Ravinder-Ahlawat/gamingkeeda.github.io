from django.contrib import admin
from django.urls import path
from . import views
# define your paths here
urlpatterns = [
    path('', views.index, name="Home"),
    path('mdview/<int:myid>', views.mdview, name="MatchDetail"),
    path('sub2', views.sub2, name="submit2"),
    path('termsandconditions/', views.tandc, name="Terms"),
    path('mdview/sub', views.joinnow, name="Submit"),
    path('asd/', views.asd, name="profile"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
    path('moregames/', views.csoon, name="MoreGames"),
    path('contact/', views.contact, name="CountactUs"),
    path('handlerequest/fordel', views.delforpay, name="fordel"),
    path('loginpage/', views.loginpage, name="loginpage"),
]