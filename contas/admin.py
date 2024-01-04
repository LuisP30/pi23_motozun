from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from contas.forms import UserCreationForm
from contas.models import MyUser

class MyUserAdmin(UserAdmin):#customização do admin pro usuario
   # add_form = UserCreationForm
    ordering = ['email']
    model = MyUser
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Disponibilidade', {'fields': ('disponibilidade',)}),
)
    #quando cria um usuario
add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
    }),
)
# barra de pesquisa no admin para fazer perquisas pelo parametro abaixo
search_fields = ('email', 'first_name', 'last_name')
ordering = ('email',)
readonly_fields = ('last_login', 'date_joined',)

#registrando o modelo
admin.site.register(MyUser, MyUserAdmin)

