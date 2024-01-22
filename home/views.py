from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def home(request):
    print("Home app1!")
    return render(
        request,
        "index.html"
    )