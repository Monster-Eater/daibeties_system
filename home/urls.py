from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name="home"),
    path('reports', views.reports, name='reports'),
    path("about", views.about, name="about"),
    path("bmi", views.bmi, name="bmi"),
    path("donate", views.donate, name="donate"),
    path("predict", views.predict, name="predict"),
    path("result", views.result, name="result"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register_user, name="register"),
    path("update_user", views.update_user, name="update_user"),
    path("update_password", views.update_password, name="update_password"),
]
