from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from django.views.decorators.csrf import csrf_exempt

import json


def add_user(request):

    AddForm = AddUser(request.POST or None)
    error = 'None'

    if 'id' in request.session:
        return redirect("/error")

    elif request.POST:

        with open("JSON/users.json", 'rb') as read_file_json:
            users = json.load(read_file_json)
        req = request.POST
        Login = req.get("login")
        Pass = req.get("password")

        for user in users['users']:
            if user['login'] == Login:
                error = 'Пользователь уже зрегистрирован'

        if error == 'None':
            users['users'].append({
                "login": Login,
                "id": len(users['users']) + 1,
                "password": Pass,
                "position": "user",
                "status": "true"
            })

            with open('JSON/users.json', 'w', encoding='utf-8') as read_file_json:
                read_file_json.write(json.dumps(users, ensure_ascii=False, separators=(',', ': '), indent=2))

            request.session.set_expiry(86400)
            request.session['id'] = users['users'][-1]['id']
            request.session['login'] = users['users'][-1]['login']
            request.session['position'] = users['users'][-1]['position']
            request.session['status'] = users['users'][-1]['status']

            return redirect("/account")

    return render(request, "user/add_user.html", {
        'form': AddForm,
         'error': error
    })


def add_mod(request):
    AddForm = AddMod(request.POST or None)
    error = 'None'
    if 'id' not in request.session:
        return redirect("/error")
    elif request.POST:
        with open("JSON/users.json", 'rb') as read_file_json:
            users = json.load(read_file_json)
        req = request.POST
        Login = req.get("login")
        Pass = req.get("password")

        for user in users['users']:
            if user['login'] == Login:
                error = 'Пользователь уже зрегистрирован'

        if error == 'None':
            users['users'].append({
                "login": Login,
                "id": len(users['users']) + 1,
                "password": Pass,
                "position": "moderator",
                "status": "true"
            })

            with open('JSON/users.json', 'w', encoding='utf-8') as read_file_json:
                read_file_json.write(json.dumps(users, ensure_ascii=False, separators=(',', ': '), indent=2))
            request.session.set_expiry(86400)
            return redirect("/moderator_list")

    return render(request, "user/add_mod.html", {
        'form': AddForm,
        'error': error
    })



def list_del_user(request):
    if "id" not in request.session or request.session['status'] == 'false':
        return redirect("/error")
    else:
        with open("JSON/users.json", encoding='utf-8') as read_file_json:
            users = json.load(read_file_json)
        data = users['users']
    return render(request, "user/del_user.html", {'data': data})



def del_user1(request, user_id):
    if "id" not in request.session or request.session['status'] == 'false':
        return redirect("/error")
    with open("JSON/users.json", encoding='utf-8') as read_file_json:
        users = json.load(read_file_json)
    users['users'][int(user_id) - 1]['status'] = 'false'
    with open('JSON/users.json', 'w', encoding='utf-8') as read_file_json:
        read_file_json.write(json.dumps(users, ensure_ascii=False, separators=(',', ': '), indent=2))
    return redirect("/list_del_user")



def moderator_list(request):
    if "id" not in request.session or request.session['status'] == 'false':
        return redirect("/error")
    else:
        with open("JSON/users.json", encoding='utf-8') as read_file_json:
            users = json.load(read_file_json)
        data = users['users']
    return render(request, "user/moderator_list.html", {
        'data': data
    })



def user_list(request):
    if "id" not in request.session or request.session['status'] == 'false':
        return redirect("/error")
    else:
        with open("JSON/users.json", encoding='utf-8') as read_file_json:
            users = json.load(read_file_json)
        data = users['users']
    return render(request, "user/user_list.html", {
        'data': data
    })
