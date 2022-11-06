from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse('lexicon:result'))
    return render(request, 'lexicon/index.html')


def result(request):
    if request.method == "POST":
        data = request.POST
        submitted_text = data.get('submitted_text')
        # for key, content in request.POST:
        #     context[key] = {content}
        return render(request, 'lexicon/result.html', {'submitted_text': submitted_text})
    return HttpResponseRedirect(reverse('lexicon:index'))
