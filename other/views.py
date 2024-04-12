from django.shortcuts import render
from datetime import datetime
from django.views import View
from django.http import HttpResponse
from random import random


class CurrentDateView(View):
    """
    Возврощает пользователю текущее время
    """

    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class RandomCountView(View):
    def get(self, request):
        ran_count = f"Генерация случайного числа :{random()}"
        return HttpResponse(ran_count)


class HelloWordView(View):
    def get(self, request):
        html = f"<h1>Hello, World</h1>"
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')
