from django.shortcuts import render


def account(request):
    mapping = {
        'moderator': "account_moderator",
        'admin': "account_admin",
        'user': "account_user",
    }

    page = 'account'
    position = request.session['position']

    if success(request):
        page = "error_404"
    elif (position in mapping.keys()):
        page = mapping[position]

    page = "account/" + page + ".html"

    return render(request, page, {})

def index(request):

    position = request.session['position']

    page = "account/account.html"

    if not success(request):
        page = "error_404"

    return render(request, page, {
        'position' : position
    })


def success(request):
    resp = ("id" not in request.session or request.session['status'] == 'false')

    return resp
