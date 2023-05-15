from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')


def base_layout(request):
    # return HttpResponse('homepage')
    return render(request, 'base_layout.html')


def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')
