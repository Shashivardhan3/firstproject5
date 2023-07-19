from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def cricket(request):
    return HttpResponse('<h1><marquee>champion team INDIA</marquee></h1>')


def ipl(request):
    return HttpResponse('<i>champion team KKR</i>')

