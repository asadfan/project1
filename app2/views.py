from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kohli(request):
    return HttpResponse('<h1 color="red">This is blr page</h1>')