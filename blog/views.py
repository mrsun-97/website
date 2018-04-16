from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def hello(request):
        return HttpResponse('<hr><hr>Hello World!<hr><hr>')
