from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, UpdateView

from registration_system.models import Funcionario

from .forms import FormularioDeCriacao

# Create your views here.


class HomeTemplateViews(TemplateView):
    template_name = 'website/pages/home.html'


def listar_funcionario(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "website/pages/listar.html", context={
        'funcionarios': funcionarios,
    })


def criar_funcionarioView(request):
    cadastro_funcionario = request.session.get('cadastro_funcionario')
    form = FormularioDeCriacao(cadastro_funcionario)
    return render(request, "website/pages/form.html", context={
        'form': form,
        'form_action': reverse('website:create')
    })


def criar_funcionario(request):
    if not request.POST:
        raise Http404
    POST = request.POST
    request.session['cadastro_funcionario'] = POST
    form = FormularioDeCriacao(POST)
    if form.is_valid():
        form.save()
        del (request.session['cadastro_funcionario'])
        return redirect(reverse('website:home'))
    return redirect(reverse('website:home'))


class FuncionarioUpdateViews(UpdateView):
    template_name = 'website/pages/atualizar.html'
    model = Funcionario
    fields = [
        'nome',
        'sobrenome',
        'tempo_de_servico',
        'remuneracao',
    ]

    def get_object(self, queryset=None):
        funcionario = None
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if id is not None:
            funcionario = Funcionario.objects.filter(id=id).first()
        elif slug is not None:
            campo_slug = self.get_slug_field()
            funcionario = Funcionario.objects.filter(**{campo_slug: slug}).first()  # noqa
        return funcionario


class FuncionarioDeleteViews(DeleteView):
    model = Funcionario
    context_object_name = 'funcionario'
    template_name = 'website/pages/excluir.html'

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     id = self.kwargs.get('id')
    #     qs = qs.filter(id=id)
    #     return qs
    #     # return redirect(reverse('website:home'))
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'form_action': reverse('website:home')
        })
        return ctx
