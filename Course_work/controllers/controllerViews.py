from django.shortcuts import render
from django.shortcuts import redirect

from Course_work.components.forms import *
from Course_work.components.data_base import *


def home(request):
    airports = data_base_load("JSON/airports.json")
    len_air = len(airports['airports'])
    num_cell = len_air + (len_air % 3)
    if len_air % 3 == 0:
        p = 0
    elif len_air % 3 == 1:
        p = 2
    elif len_air % 3 == 2:
        p = 1
    len_air_r = len_air + p
    air_list = []

    for i in range(0, len_air_r - 3, 3):
        rand_str = [airports['airports'][i], airports['airports'][i + 1], airports['airports'][i + 2]]
        air_list.append(rand_str)
    if p == 0:
        air_list.append([airports['airports'][len_air_r - 3], airports['airports'][len_air_r - 2],
                         airports['airports'][len_air_r - 1]])
    elif p == 1:
        air_list.append([airports['airports'][len_air_r - 3], airports['airports'][len_air_r - 2], 0])
    elif p == 2:
        air_list.append([airports['airports'][len_air_r - 3], 0, 0])

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
        users = data_base_load("JSON/users.json")
        req = request.POST
        # Проверка входа в систему
        Login = req.get("login")
        Pass = req.get("password")
        error = 'Неправильно введён логин или пароль'
        #       checkFunc = "none"

        for user in users['users']:
            if user['login'] == Login and user['password'] == Pass:
                request.session.set_expiry(86400)
                request.session['id'] = user['id']
                request.session['login'] = user['login']
                request.session['position'] = user['position']
                request.session['status'] = user['status']
                return redirect("/account")

    return render(request, 'login.html', {
        'form': logForm,
        'error': error
    })


def logout(request):
    request.session.clear()
    return redirect("/")
