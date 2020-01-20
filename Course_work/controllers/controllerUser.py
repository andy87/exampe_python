from django.shortcuts import render
from django.shortcuts import redirect

from Course_work.components.forms import *
from Course_work.models.ModelUser import *



def add_user(request):

    if request.POST:
        data = ModelUser.create(ModelUser(), request)
        return redirect(data["redirect"])

    return render(request, ModelUser.PAGE_ADD, {
        'form': AddUser(request.POST or None),
        'error': 'None'
    })



def add_mod(request):
    AddForm = AddMod(request.POST or None)
    error = 'None'

    if assessUser(request):
        return redirect("/error")

    elif request.POST:
        users = data_base_load("JSON/users.json")
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

            data_base_update('JSON/users.json', users)

            request.session.set_expiry(86400)
            return redirect("/moderator_list")

    return render(request, "user/add_mod.html", {
        'form': AddForm,
        'error': error
    })


def list_del_user(request):
    if assessAdmin(request):
        return redirect("/error")
    else:
        users = data_base_load("JSON/users.json")
        data = users['users']
    return render(request, "user/del_user.html", {'data': data})


def del_user1(request, user_id):
    if assessAdmin(request):
        return redirect("/error")
    users = data_base_load("JSON/users.json")
    users['users'][int(user_id) - 1]['status'] = 'false'

    data_base_update('JSON/users.json', users)

    return redirect("/list_del_user")


def moderator_list(request):
    if assessAdmin(request):
        return redirect("/error")
    else:
        users = data_base_load("JSON/users.json")
        data = users['users']

    return render(request, "user/moderator_list.html", {
        'data': data
    })


def user_list(request):
    if assessAdmin(request):
        return redirect("/error")
    else:
        users = data_base_load("JSON/users.json")
        data = users['users']
    return render(request, "user/user_list.html", {
        'data': data
    })


def assessUser(request):
    return ("id" not in request.session)

def assessAdmin(request):
    return ("id" not in request.session or request.session['status'] == 'false')

