
from django.shortcuts import render

from Course_work.models.ModelAirport import *


def air_detail(request, air_id):

    data = ModelAirport.detail(ModelAirport(), (int(air_id)-1))

    return render(request, "airport/air_detail.html", data)