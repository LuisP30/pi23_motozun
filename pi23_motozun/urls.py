from django.contrib import admin
from django.urls import path, include
from viagem.views import *

urlpatterns = [
    path('', home , name='home'),
    path('viagem/', include('viagem.urls')),
    path('auth/', include('contas.urls')),
    path('admin/', admin.site.urls),
   

]
