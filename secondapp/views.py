from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jam(request):
    return HttpResponse("Hi Kohli")