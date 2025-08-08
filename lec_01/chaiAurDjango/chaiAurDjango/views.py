from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("I am Home page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("I am about page")
    return render(request, 'website/about.html')


def contact(request):
    # return HttpResponse("I am contact page")
    return render(request, 'website/contact.html')
