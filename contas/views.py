from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from .models import MyUser
from pi23_motozun import roles
from rolepermissions.roles import assign_role



from contas.forms import CustomUserCreationForm


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        # se o usuario existir , faz o login
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email ou senha inválidos')
    # Se o Usuario estiver autenticado
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')

#registrar usuario
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = MyUser.objects.filter(email=request.POST['email']).get()
            if int(request.POST['cargo']) == 1:
                assign_role(usuario, roles.Passageiro)
            else:
                assign_role(usuario, roles.Mototaxista)
            return render(request, 'login.html') # Redirecione para a página de login
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

def escolhercadastro(request):
    return render (request, 'escolhercadastro.html')