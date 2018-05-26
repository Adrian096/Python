from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    name = request.GET.get("name")
    return HttpResponse("Hello "+name)
