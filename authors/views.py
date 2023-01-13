from django.shortcuts import render
from .forms import RegisterForm

def register(request):

    forms = RegisterForm()
    return render(request,'authors/pages/register_user.html', {'form':forms})
