from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView

class tutorial(RedirectView): url = 'https://data-flair.training/blogs/category/django/'

def index(request):
    return HttpResponse("<h1>Data Flair Django</h1>Hello, you just configured your First URL")


def data_flair(request):
    return redirect('/dataflair')


def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    html.set_cookie('dataflair', 'Hello this is your Cookies', max_age=None)
    return html

def showcookie(request):
    show = request.COOKIES['dataflair']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)