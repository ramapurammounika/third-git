from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mouni(request):
    return HttpResponse('<h1><marquee>mounika reddy</h1></marquee>')