from django.contrib import admin
from django.urls import path, include                  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("singlepage.urls")),  
    path("", include('signuppage.urls')),  
    path("", include('loginpage.urls')), 
    path("", include('statspage.urls')),         
]