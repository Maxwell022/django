#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog(request):
    print("Blog app1!")
    return HttpResponse("Está em blog app1")