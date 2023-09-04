from django.contrib import admin

from registration_system.models import Funcionario

# Register your models here.


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ['id']
