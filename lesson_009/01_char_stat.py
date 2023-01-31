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
    Сортировка: sort_by='A' - по старшинству алфавита, при sort_by='Z' - с конца алфавита,
    sort_by=9 - по возрастанию числа букв, sort_by=1 - по убыванию. """

    def __init__(self, file_name, sort_by):
        self.column_width = 0
        self.sort_by = sort_by
        self.total_value = 0
        self.file_name = file_name
        self.stat = {}
        self.cyrillic = {}
        self.sorted_list = []
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
                self.total_value += value
                self.cyrillic[chr(code)] = value
        self.column_width = len(str(self.total_value)) + 4
        self.frame()

    def frame(self):
        match_list = [1, 9, 'A', 'Z']
        if self.sort_by not in match_list:
            print('Sort_by error. You must enter int 1 or 9 for frequency or A, Z for lettering.')
        else:
            column_width, column1_sign, column2_sign, end_sign = self.column_width, 'буква', 'частота', 'итого'
            edge = '{plus}{line}{plus}{line}{plus}'.format(plus='+', line='-' * column_width)
            head = f'|{column1_sign: ^{column_width}}|{column2_sign: ^{column_width}}|'
            print(f'{edge}\n{head}\n{edge}')
            self.method_choosing()
            end = f'|{end_sign: ^{column_width}}|{self.total_value: ^{column_width}}|'
            print(f'{edge}\n{end}\n{edge}')

    def method_choosing(self):
        if self.sort_by == 1:
            self.sort_list(reverse=False)
            for letter, value in self.sorted_list:
                print(f'|{letter: ^{self.column_width}}|{value: ^{self.column_width}}|')
        elif self.sort_by == 9:
            self.sort_list(reverse=True)
            for letter, value in self.sorted_list:
                print(f'|{letter: ^{self.column_width}}|{value: ^{self.column_width}}|')
        elif self.sort_by == 'Z':
            for letter in sorted(self.cyrillic, reverse=True):
                print(f'|{letter: ^{self.column_width}}|{self.cyrillic[letter]: ^{self.column_width}}|')
        elif self.sort_by == 'A':
            for letter, value in sorted(self.cyrillic.items()):
                print(f'|{letter: ^{self.column_width}}|{value: ^{self.column_width}}|')

    def sort_list(self, reverse):
        sorted_tuple = sorted(self.cyrillic, key=self.cyrillic.get, reverse=reverse)
        for key in sorted_tuple:
            value = key, self.cyrillic[key]
            self.sorted_list.append(value)


AlphaStat(file_name='voyna-i-mir.txt.zip', sort_by='y')
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
