from django.shortcuts import render, get_list_or_404,get_object_or_404, redirect
from .forms import RegisterForm
from django.http import Http404


def registro(request):
    register_form_data = request.session.get('register_form_data',None)
    forms = RegisterForm(register_form_data)
    return render(request,"authors/register_user.html",{'forms':forms,})

def criar(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    return redirect('authors:register')
