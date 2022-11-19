from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from smartapp.lexicon import lexicon_logic
import string, nltk
from nltk.corpus import stopwords


def remove_punctuations_func(text: str):
    punctuation = string.punctuation
    new_text = [letter for letter in text]
    for i in range(0, len(new_text)):
        if new_text[i] in punctuation:
            new_text[i] = ''
        else:
            continue
    modified_text = "".join(new_text)
    return modified_text


def upper_case_func(text: str):
    new_text = text.upper()
    return new_text


def lower_case_func(text: str):
    new_text = text.lower()
    return new_text


def new_line_remove_func(text: str):
    return "".join(text.splitlines())


def extra_space_remove_func(text: str):
    new_text = [letter for letter in text]
    for i in range(0, len(new_text)):
        if new_text[i] == ' ':
            new_text[i] = ''
        else:
            continue
    text_without_space = "".join(new_text)
    return text_without_space


def count_characters_func(text: str):
    new_text = [letter for letter in text]
    counter = 0
    for i in range(0, len(new_text)):
        if new_text[i] == ' ':
            continue
        else:
            counter += 1
    return counter


def index(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse('lexicon:result'))
    return render(request, 'lexicon/index.html')


def result(request):
    if request.method == "POST":
        data = request.POST
        submitted_text = data.get('submitted_text')
        remove_punctuations = data.get('remove_punctuations')
        upper_case = data.get('upper_case')
        new_line_remove = data.get('new_line_remove')
        extra_space_remove = data.get('extra_space_remove')
        count_characters = data.get('count_characters')
        changed_text = submitted_text
        character_count = 0

        if remove_punctuations == "on":
            changed_text = remove_punctuations_func(changed_text)
        if upper_case == "on":
            changed_text = upper_case_func(changed_text)
        if new_line_remove == "on":
            changed_text = new_line_remove_func(changed_text)
        if extra_space_remove == "on":
            changed_text = extra_space_remove_func(changed_text)
        if count_characters == "on":
            character_count = count_characters_func(changed_text)

        return render(request, 'lexicon/result.html',
                      {'submitted_text': submitted_text,
                       'changed_text': changed_text,
                       'character_count': character_count
                       })
    return HttpResponseRedirect(reverse('lexicon:index'))


