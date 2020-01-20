from django.shortcuts import render

from Course_work.models.ModelOrder import *



def add_order(request):
    return render(request, ModelOrder.PAGE_ADD)
