from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


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
    return render(request, 'authors/login.html')


def login_create(request):
    return render(request, 'authors/login.html')
