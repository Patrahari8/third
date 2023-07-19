from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_string(request):
    return HttpResponse('this is first response')
def second_string(request):
    return HttpResponse('this is second response')
def third_string(request):
    return HttpResponse('this is third response')
def fourth_string(request):
    return HttpResponse('try try try try')
