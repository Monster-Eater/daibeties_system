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
    path("report_pdf", views.report_pdf, name="report_pdf"),     
    path('profile/<int:pk>', views.profile, name = 'profile' ),
]
