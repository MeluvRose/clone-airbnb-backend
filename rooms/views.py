from django.shortcuts import render
from django.http import HttpResponse


def say_Hello(request):
    return HttpResponse("hello")
