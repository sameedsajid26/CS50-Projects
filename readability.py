from cs50 import get_string
import string


def main():
    text = get_string("Text: ")

    if index(count_letters(text), count_words(text), count_sentences(text)) >= 1 and index(count_letters(text), count_words(text), count_sentences(text)) <16:
        print(f"Grade {index(count_letters(text), count_words(text), count_sentences(text))}")

    elif index(count_letters(text), count_words(text), count_sentences(text)) < 1:
        print("Before Grade 1")

    elif index(count_letters(text), count_words(text), count_sentences(text)) >= 16:
        print("Grade 16+")


def count_letters(s):

    letters = 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c in string.punctuation and c.isspace():
            letters += 0

    return letters


def count_words(t):

    words = 1

    for c in t:
        if c.isspace():
            words += 1

    return words


def count_sentences(u):
    sentences = 0
    for c in u:
        if c == '.' or c == '!' or c == '?':
            sentences += 1
    return sentences


def index(letters, words, sentences):
    L = letters * 100 / words
    S = sentences * 100 / words

    grade_level = round(0.0588 * L - 0.296 * S - 15.8)
    return grade_level


main()