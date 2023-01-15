import re

from django.core.exceptions import ValidationError


# Forma 3
def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

# Verificação de senha


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'A senha precisa ter uma letra maiúscula, '
            'uma letra minúscula e números.'
            'Precisa ter no mínimo 8 caracteres.'
        ),
            code='Invalid'
        )
