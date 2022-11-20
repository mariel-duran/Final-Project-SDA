from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import lexicon_logic
import string, nltk
from nltk.corpus import stopwords


def index(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse('lexicon:result'))
    return render(request, 'lexicon/index.html')


def result(request):
    if request.method == "POST":
        data = request.POST
        submitted_text = data.get('submitted_text')
        remove_punctuations = data.get('remove_punctuations')
        upper_lower = data.get('upper_lower')
        new_line_remove = data.get('new_line_remove')
        extra_space_remove = data.get('extra_space_remove')
        count_characters = data.get('count_characters')
        spell_check = data.get('spell_check')
        generate_summary = data.get('generate_summary')
        remove_stop_words = data.get('remove_stop_words')
        changed_text = submitted_text

        character_count = 0
        misspelled_dict = {}
        summary_word_dict = {}

        # options that affect the text directly
        if remove_punctuations == "on":
            changed_text = lexicon_logic.remove_punctuations_func(changed_text)
        if upper_lower == "upper_case":
            changed_text = lexicon_logic.upper_case_func(changed_text)
        else:
            changed_text = lexicon_logic.lower_case_func(changed_text)
        if new_line_remove == "on":
            changed_text = lexicon_logic.new_line_remove_func(changed_text)
        if extra_space_remove == "on":
            changed_text = lexicon_logic.extra_space_remove_func(changed_text)
        if remove_stop_words == "on":
            changed_text = lexicon_logic.remove_stop_words_func(changed_text)

        # other functions
        if count_characters == "on":
            character_count = lexicon_logic.count_characters_func(changed_text)

        if spell_check == "on":
            misspelled_dict = lexicon_logic.spell_check_func(changed_text)

        if generate_summary == "on":
            summary_word_dict = lexicon_logic.generate_summary_of_word_func(changed_text)





        return render(request, 'lexicon/result.html',
                      {'submitted_text': submitted_text,
                       'changed_text': changed_text,
                       'character_count': character_count,
                       'mispelled_dict': misspelled_dict,
                       'summary_word_dict': summary_word_dict,
                       })
    return HttpResponseRedirect(reverse('lexicon:index'))


