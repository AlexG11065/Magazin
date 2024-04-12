from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from random import random


class LoginIndexView(View):
    def get(self, request):
        return render(request, 'index.html')

