from django.urls import path, include
from . import views


urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    # path('', views.account, name="Register"),
    path('register', views.register, name="Register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="Logout"),
    # path('asd/<int:myid>', views.asd, name="asd"),
    # path('asd/aj', views.aj, name="aj"),
    path('register2', views.register2, name="register2"),
    path('pubgin', views.pubgin, name="pubgin"),
]