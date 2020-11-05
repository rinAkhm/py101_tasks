import sys
import argparse 
from nltk.corpus import stopwords
import collections


"""
Программа считает Топ-100 слов для переданного ей текстого файла.
Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk
Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

def exclude_stop_words(text):
# функция исключает стоп слова из ипортированного списка nltk 
    stop_words = stopwords.words ("russian")
    list_without_stop_words = []
    for word in text:
        if word  not in stop_words:
            list_without_stop_words.append(word)
    return list_without_stop_words

def create_parser():
#Функция считывает название файла через консоль и открывает этот файл. 
#второй параметор позволяет выбрать количество чисел для считывания
    parser = argparse.ArgumentParser()
    parser.add_argument('-b','--book', type=argparse.FileType(encoding='utf-8'), help='you need write name file', default='book.txt')
    parser.add_argument ('count', nargs='?', type = int, default=100)
    return parser

def create_clean_list(text):
#Функция разбирает текст на слова, избавляет текст от
#  символов и цифр, после сохраняет его в список. 
    list_without_symbols = []
    for word in text.lower().split():
        symbols = '-!@#№$<>%^"\'*.()_+="№;:,?'
        for symbol in range(0,len(symbols)):
            word = word.replace(symbols[symbol],"")
        if word.isalpha():
            list_without_symbols.append(word)
    return list_without_symbols
 
if __name__ == '__main__':
    word_list = []
    dictionary = {}
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    text = " ".join(namespace.book.readlines())
    count = namespace.count

#добавляем слова в словарь 
    for word_dictionary in exclude_stop_words(create_clean_list(text)): 
        dictionary.setdefault (word_dictionary, 0)
        dictionary[word_dictionary] +=1

#сортируем словарь и выводим в принт
    top_word = collections.Counter(dictionary).most_common(count)
    print(top_word)
 