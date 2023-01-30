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


class Chatterer:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}


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
        pprint(self.stat)





    # def prepare(self):
    #     self.totals = {}
    #     self.stat_for_generate = {}
    #     for sequence, char_stat in self.stat.items():
    #         self.totals[sequence] = 0
    #         self.stat_for_generate[sequence] = []
    #         for char, count in char_stat.items():
    #             self.totals[sequence] += count
    #             self.stat_for_generate[sequence].append([count, char])
    #             self.stat_for_generate[sequence].sort(reverse=True)
    #
    # def chat(self, N, out_file_name=None):
    #     N = 1000
    #     printed = 0
    #     if out_file_name is not None:
    #         file = open(out_file_name, 'w', encoding='utf8')
    #     else:
    #         file = None
    #
    #     sequence = ' ' * self.analize_count
    #     spaces_printed = 0
    #     while printed < N:
    #         char = self._get_char(char_stat=self.stat_for_generate[sequence], total=self.totals[sequence])
    #         if file:
    #             file.write(char)
    #         else:
    #             print(char, end='')
    #         if char == ' ':
    #             spaces_printed += 1
    #             if spaces_printed >= 10:
    #                 if file:
    #                     file.write('\n')
    #                 else:
    #                     print()
    #                 spaces_printed = 0
    #         printed += 1
    #         sequence = sequence[1:] + char
    #     if file:
    #         file.close()
    #
    # def _get_char(self, char_stat, total):
    #     dice = randint(1, total)
    #     pos = 0
    #     for count, char in char_stat:
    #         pos += count
    #         if dice <= pos:
    #             break
    #     return char


chatterer = Chatterer(file_name='voyna-i-mir.txt.zip')
chatterer.collect()
# chatterer.prepare()
# chatterer.chat(N=10000, out_file_name='out.txt')

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
