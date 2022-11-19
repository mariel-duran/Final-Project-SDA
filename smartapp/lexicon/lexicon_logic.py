import string, nltk
from nltk.corpus import stopwords
from spellchecker import SpellChecker

nltk.download('stopwords')

text_example = '''
my nime is mariel. 
I live in Estonia! 
Im form Donican Republic
'''


def remove_punctuations(text: str):
    punctuation = string.punctuation
    new_text = [letter for letter in text]
    for i in range(0, len(new_text)):
        if new_text[i] in punctuation:
            new_text[i] = ''
        else:
            continue
    modified_text = "".join(new_text)
    return modified_text


def upper_case(text: str):
    new_text = text.upper()
    return new_text


def lower_case(text: str):
    new_text = text.lower()
    return new_text


def new_line_remove(text: str):
    return "".join(text.splitlines())


def extra_space_remove(text: str):
    new_text = [letter for letter in text]
    for i in range(0, len(new_text)):
        if new_text[i] == ' ':
            new_text[i] = ''
        else:
            continue
    text_without_space = "".join(new_text)
    return text_without_space


def count_characters(text: str):
    new_text = [letter for letter in text]
    counter = 0
    for i in range(0, len(new_text)):
        print(new_text[i])
        if new_text[i] == ' ':
            continue
        else:
            counter += 1
    return counter


def spell_check(text: str):
    # I want to have the output text to be same as input text but with spell checks, meaning I keep punctuation and
    # case.
    spell = SpellChecker()
    words = new_line_remove(remove_punctuations(text)).split()
    mispelled = spell.unknown(words)
    for word in mispelled:
        print(word)
        new_word = spell.correction(word)
        print(new_word)
    correct_text = "".join(mispelled)
    return correct_text


def generate_summary_of_word(text:str):
    pass


def remove_stop_words(text: str):
    new_text = [letter for letter in text]
    for i in range(0, len(new_text)-1):
        if new_text[i] in stopwords.words('english'):
            new_text.pop(i)
        else:
            continue
    text_without_stopwords = "".join(new_text)
    return text_without_stopwords


print(spell_check(text_example))