from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = HttpResponse()
    response.writelines("<h1>Welcome</h1>")
    response.write("Đây là app home")
    return response