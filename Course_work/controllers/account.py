from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import json



def account(request):
    page = 'account.html'
    if "id" not in request.session or request.session['status'] == 'false':
        page = "error_404.html"
    elif request.session['position'] == 'user':
        page = 'account_user.html'
    elif request.session['position'] == 'admin':
        page = 'account_admin.html'
    elif request.session['position'] == 'moderator':
        page = 'account_moderator.html'

    page = "account/" + page

    return render(request, page, {})

