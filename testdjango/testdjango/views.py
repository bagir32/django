from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView

class tutorial(RedirectView): url = 'https://data-flair.training/blogs/category/django/'

def index(request):
    return HttpResponse("<h1>Data Flair Django</h1>Hello, you just configured your First URL")


def data_flair(request):
    return redirect('/dataflair')