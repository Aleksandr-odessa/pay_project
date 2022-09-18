from django.shortcuts import render
from django.http import JsonResponse
from .request_item import request_item

def index(request):
    return render(request, "payments/index.html", {'hello':'Добро пожаловать на сайт-проверку'})

def detail(request, item_id):
    return render(request, "payments/index.html", request_item('detail', item_id))

def buy (request, buy_id):
        return JsonResponse(request_item('buy', buy_id))
