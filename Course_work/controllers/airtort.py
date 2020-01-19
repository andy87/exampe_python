from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import json




def air_detail(request, air_id):
    with open("JSON/airports.json", encoding='utf-8') as read_file_json:
        air = json.load(read_file_json)

    name = air['airports'][int(air_id)-1]['name']
    flights = air['airports'][int(air_id)-1]['flights']

    return render(request, "airport/air_detail.html", {
        "name": name, "flights": flights
    })

