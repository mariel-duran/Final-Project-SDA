import string

text_example = 'my name is mariel. I live in Estonia! Im from Dominican Republic'


def remove_punctuations(text:str):
    punctuation = string.punctuation
    new_text = [letter for letter in text]
    for i in range(0, len(new_text)):
        if new_text[i] in punctuation:
            new_text[i] = ''
        else:
            continue
    modified_text = "".join(new_text)
    return modified_text


def upper_case(text:str):
    new_text = text.upper()
    return new_text


def lower_case(text:str):
    new_text = text.lower()
    return new_text

