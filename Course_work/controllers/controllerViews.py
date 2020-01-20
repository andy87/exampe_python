from django.shortcuts import render
from django.shortcuts import redirect

from Course_work.components.forms import *
from Course_work.models.ModelAirport import *
from Course_work.models.ModelUser import *


def home(request):

    air_list = ModelAirport.getAirLineList(ModelAirport())

    return render(request, 'home.html', {
        'air_list': air_list
    })


def error404(request):
    return render(request, 'error_404.html', {})


def login(request):
    logForm = LoginForm(request.POST or None)
    error = 'None'
    if 'id' in request:
        return redirect("/error")

    if request.POST:
        if (ModelUser.Authorize(ModelUser(), request)):
            return redirect("/account")

    return render(request, 'login.html', {
        'form': logForm,
        'error': error
    })


def logout(request):
    request.session.clear()
    return redirect("/")
