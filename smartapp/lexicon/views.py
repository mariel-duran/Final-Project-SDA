from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request,'lexicon/index.html')

def result(request):
    context = {}
    return render(request, 'lexicon/result.html')

