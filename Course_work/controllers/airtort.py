
from django.shortcuts import render

from Course_work.components.data_base import *


def air_detail(request, air_id):

    air = data_base_load("JSON/airports.json")

    name = air['airports'][int(air_id)-1]['name']
    flights = air['airports'][int(air_id)-1]['flights']

    return render(request, "airport/air_detail.html", {
        "name": name, "flights": flights
    })