from django import forms
from .models import Cliente,Endereco

class ClientForm(forms.ModelForm):
    # alterando um valor de um campo dos fields recebidos
    # nome = forms.CharField(widget=forms.Textarea())
    # sexo = Cliente.objects.get()
    class Meta:
        model = Cliente
        fields = ['nome','sexo','email','profissao','data_nascimento']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero','complemento','bairro','cidade','estado','pais']
