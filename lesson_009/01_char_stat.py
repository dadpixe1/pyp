# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile
from pprint import pprint
from random import randint


class AlphaStat:
    """ Подсчет статистики по буквам в тексте. Параметр file_name - имя и расширение файла в кавычках.
    Сортировка при alfabet=True - по старшинству алфавита,
    при alfabet=False - с конца алфавита, при alfabet='i' - переход в режим сортировки значений increase.
    Режим increase: При increase=True - по возрастанию числа букв, increase=False - по убыванию. """

    def __init__(self, file_name, alfabet, increase):
        self.total_value = 0
        self.increase = increase
        self.alfabet = alfabet
        self.file_name = file_name
        self.stat = {}
        self.stat_cyrillic = {}
        self.collect()

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
        self.sort()

    def sort(self):
        encoding = {}
        for symbol, value in self.stat.items():
            self.total_value += value
            encoding[ord(symbol)] = value
        for code, value in encoding.items():
            if code in range(1000, 1200):
                self.stat_cyrillic[chr(code)] = value
        self.frame()

    def frame(self):
        column_width = len(str(self.total_value)) + 4
        column_width, column1_sign, column2_sign, end_sign = column_width, 'буква', 'частота', 'итого'
        edge = '{plus}{line}{plus}{line}{plus}'.format(plus='+', line='-' * column_width)
        head = f'|{column1_sign: ^{column_width}}|{column2_sign: ^{column_width}}|'
        print(edge)
        print(head)
        print(edge)
        self.method_choosing(column_width=column_width)
        end = f'|{end_sign: ^{column_width}}|{self.total_value: ^{column_width}}|'
        print(edge)
        print(end)
        print(edge)

    def method_choosing(self, column_width):
        sorted_list = []
        if self.alfabet == 'i':
            sorted_tuple = sorted(self.stat_cyrillic, key=self.stat_cyrillic.get, reverse=self.increase)
            for key in sorted_tuple:
                value = key, self.stat_cyrillic[key]
                sorted_list.append(value)
        if sorted_list:
            for letter, value in sorted_list:
                self.total_value += value
                print(f'|{letter: ^{column_width}}|{value: ^{column_width}}|')
        elif not self.alfabet:
            for letter in sorted(self.stat_cyrillic, reverse=True):
                self.total_value += self.stat_cyrillic[letter]
                print(f'|{letter: ^{column_width}}|{self.stat_cyrillic[letter]: ^{column_width}}|')
        else:
            for letter, value in sorted(self.stat_cyrillic.items()):
                self.total_value += value
                print(f'|{letter: ^{column_width}}|{value: ^{column_width}}|')


AlphaStat(file_name='voyna-i-mir.txt.zip', alfabet=True, increase=True)


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
