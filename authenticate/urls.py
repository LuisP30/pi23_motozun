from django.urls import path
from authenticate.views import login, cadastro

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro')

]
