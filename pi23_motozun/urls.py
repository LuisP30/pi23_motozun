from django.contrib import admin
from django.urls import path, include
from viagem.views import home

urlpatterns = [
    path('', home, name='home'),
    path('contas/', include('contas.urls')),
    path('viagem/', include('viagem.urls')),
    path('admin/', admin.site.urls),

]
