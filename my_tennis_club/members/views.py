from django.shortcuts import render

from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello, world. You're at the members index.")

# Create your views here.
