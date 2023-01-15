from django.test import TestCase
from parameterized import parameterized

from authors.forms import RegisterForm


class AuthorRegisterFormUnitTeste(TestCase):

    @parameterized.expands([
        ('usernme', 'Seu usuário'),
        ('email', 'Ex.: email@gmail.com'),
        ('last_name', 'Ex.: Alves'),
    ])
    def test_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        placeholder_origin = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder, placeholder_origin)
