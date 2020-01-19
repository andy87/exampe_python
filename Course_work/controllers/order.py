from django.shortcuts import render


def order_add(request):
    return render(request, "order/order_add.html")
