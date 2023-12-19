from django.contrib import admin
from django.urls import path, include
from viagem.views import home

urlpatterns = [
    path('', home),
    path('viagem/', include('viagem.urls')),
    path('auth/', include('authenticate.urls')),
    path('admin/', admin.site.urls),

]
