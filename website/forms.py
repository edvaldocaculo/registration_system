from django import forms

from registration_system.models import Funcionario


class FormularioDeCriacao(forms.ModelForm):
    biografia = forms.CharField(
        label='Biografia',
        widget=forms.Textarea(attrs={
            'placeholder': 'escreva...',
            'class': 'form-control',
        }),
        required=False,
    )

    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'digite seu nome',
            }),
            'sobrenome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'digite seu sobrenome',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'digite seu CPF',
            }),
            'remuneracao': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '00,00 R$'
            })
        }
