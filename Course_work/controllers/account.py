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


def success(request):
    resp = ("id" not in request.session or request.session['status'] == 'false')

    return resp
