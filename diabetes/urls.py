from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header="The Health Prediction Admin"
admin.site.site_title= "The Health Prediction Admin Portal"
admin.site.site_header= "Wellcom Mr.Jakir Hossein"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('member/', include('members.urls')),
   
]