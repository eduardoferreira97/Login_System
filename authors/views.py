from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    forms = RegisterForm(register_form_data)
    return render(request, "authors/register_user.html", {'forms': forms, })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Sua conta foi criada, faça login')

        del (request.session['register_form_data'])

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/login.html', {
        'forms': form,
        'form_action': reverse('authors:login_create')
    })


def login_create(request):

    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        is_authenticated = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )
        if is_authenticated:
            messages.success(request, 'Você está logado')
            return redirect(login_url)

        messages.error(request, 'Credenciais inválidas')
        return redirect(login_url)
    messages.error(request, 'Erro para validar os dados')
    return redirect(login_url)
