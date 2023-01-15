import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Forma 3
def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'A senha precisa ter uma letra maiúscula '
            'uma letra minúscula e um número.'
            'Precisa ter no mínimo 8 caracteres'
        ),
            code='Invalid'
        )


class RegisterForm(forms.ModelForm):

    # Forma 3
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu usuário')
        add_placeholder(self.fields['email'], 'Ex.: email@gmail.com')
        add_placeholder(self.fields['first_name'], 'Ex.: João')
        add_placeholder(self.fields['last_name'], 'Ex.: Alves')

    # Forma 2
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Digite a sua senha'}),
        error_messages={'required': 'Senha não pode ser vazia'},
        help_text=('A senha precisa ter uma letra maiúscula, '
                   'uma letra minúscula e números.'
                   'Precisa ter no mínimo 8 caracteres'),
        validators=[strong_password]
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirme a sua senha'}),
        error_messages={'required': 'Senha não pode ser vazia'},
        help_text=('A senhas precisam ser iguais')
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password',]

    # validação do campo, caso ele entre na condição, ele envia um alerta

    def clean_password(self):

        data = self.cleaned_data.get('password')

        if 'aten' in data:
            raise ValidationError(
                'Não digite %(value)s no campo',
                code='Invalid',
                params={'value': '"aten"'}
            )

        return data

    # Verificação para ver se os password são iguais
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError({
                'password': 'As senhas precisam se iguais',
                'confirm_password': 'As senhas precisam se iguais'
            })
