from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password',]

        # Caso a quantidade de dados no formulário seja grande, user EXCLUDE para tirar apenas os campos não necessários
        # exclude = ['first_name']

        # Muda o nome da label, de username para Usuário
        labels = {'username': 'Username', 'first_name': 'First name',
                  'last_name': 'Last name', 'email': 'E-mail', 'password': 'Password'}

        help_texts = {'email': 'O e-mail precisa ser válido'}

        # Menssagens espécificas para cada campo, vai depender do tipo de mensagem e o momento que ela irá aparecer
        error_messages = {'username': {
            'required': 'Este campo não pode ser vazio', 'invalid': 'Campo inválido'}}

        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'Escreva seu nome aqui', 'class': 'input text-area'}),
                   'password': forms.PasswordInput(attrs={'placeholder': 'Escreva sua senha aqui'})}
