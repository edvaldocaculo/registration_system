from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    path('', views.HomeTemplateViews.as_view(), name='home'),
    path('cadastrar/', views.criar_funcionarioView, name='cadastrarViews'),
    path('cadastrar/create/', views.criar_funcionario, name='create'),
    path('funcionarios/lista/', views.listar_funcionario, name='listar_fun'),
    path('funcionario/atualizar/<int:pk>',
         views.FuncionarioUpdateViews.as_view(), name='atualizar_fun'),
    path('funcionario/deletar/<int:pk>',
         views.FuncionarioDeleteViews.as_view(), name='excluir_fun'),
]
