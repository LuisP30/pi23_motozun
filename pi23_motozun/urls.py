from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('', home),
    path('solicitar/', include('core.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('admin/', admin.site.urls),

]
