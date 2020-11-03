import sys
import argparse


"""
Программа считает Топ-100 слов для переданного ей текстого файла.
Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk
Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b','--book', type=argparse.FileType(), help='you need write name file',default='111.txt')
    return parser

if __name__ == '__main__':
#position argument
    word_list = []
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    text = namespace.book.read()
    for each_word in text.split():
        word_list.append(each_word)
        print(each_word)