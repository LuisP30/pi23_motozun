from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('', home),
    path('authenticate/', include('authenticate.urls')),
    path('admin/', admin.site.urls),
    
]
