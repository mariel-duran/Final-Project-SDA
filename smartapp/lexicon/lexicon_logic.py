import string, nltk
from nltk.corpus import stopwords
from spellchecker import SpellChecker

# if stopwords have not been downloaded:
# nltk.download('stopwords')

text_example = '''
my nime is mariel. 
I live in Estonia! 
Im form Donican Republic
'''


def remove_punctuations_func(text: str):
    punctuation = string.punctuation
    new_text = [letter for letter in text]
    for i in range(len(new_text)):
        if new_text[i] in punctuation:
            new_text[i] = ''
        else:
            continue
    modified_text = "".join([word for word in new_text])
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
    for i in range(len(new_text)):
        print(new_text[i])
        if new_text[i] == ' ':
            continue
        else:
            counter += 1
    return counter


def spell_check_func(text: str):
    spell = SpellChecker()
    words = remove_punctuations_func(text).split()
    misspelled = spell.unknown(words)
    misspelled_options = {}
    for word in misspelled:
        misspelled_options[word] = [spell.correction(word), spell.candidates(word)]
    return misspelled_options


def generate_summary_of_word_func(text:str):
    pass


def remove_stop_words_func(text: str):
    unchecked_text = text.split()
    stopwords_list = stopwords.words('english')
    print(stopwords_list)
    length_text = len(unchecked_text)
    hold_non_stopwords = []
    for i in range(length_text):
        if unchecked_text[i].lower() in stopwords_list:
            continue
        else:
            hold_non_stopwords.append(unchecked_text[i])
    text_without_stopwords = "".join([word + " " for word in hold_non_stopwords])
    return text_without_stopwords


print(spell_check_func(text_example))