from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('register',v.adduser,name="reg"),
    path('login',v.login_view,name="login"),
    path('logout',v.logout_view,name="logout"),
    path('editprofile',v.edit_profile,name="editprofile"),
]
