from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Its a blog homepage</h1>')


def about(request):
    return HttpResponse('<h1>Its a blog about page</h1>')
