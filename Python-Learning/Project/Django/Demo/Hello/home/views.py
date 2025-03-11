from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('This is Home PAge')


def about(request):
    return HttpResponse('This is About Page')


def services(request):
    return HttpResponse('This is Service Page')


def portfolio(request):
    return HttpResponse('This is Portfolio Page')


def contact(request):
    return HttpResponse('This is Contact Page')
