from urllib import response
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseServerError


# Create your views here.

def home(request):
    #return HttpResponse("<h1>Blog home</h1>")
    return render(request, 'blog/home.html')

def about(request):
    #return HttpResponse("<h1>Blog About</h1>") 
    return render(request, 'blog/about.html')

def error(request):
    test1 = 1 + 1/0
    # try:
    #     #print(1/0)
    #     test = 1/0
    # except ValueError as e:
    #     #raise HttpResponseServerError(e.__class__)
    #     pass
    # return response("Hello")

def error4(request):
    raise Http404('Very Bad Request')