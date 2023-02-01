# -*- coding: utf-8 -*-

from pprint import pprint
import zipfile

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class LogPaser:
    """ Smthng. """

    def __init__(self, file_to_read, file_to_write, event):
        self.file_to_write = file_to_write
        self.file_name = file_to_read
        self.event = event
        self.log_list = []
        self.list_to_print = []
        self.log_collect()

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def log_collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.log_list.append(line)
        self.event_extracting()

    def event_extracting(self):
        temp, event_value = [], 0
        for line in self.log_list:
            if self.event in line:
                item = line.split(' ')
                temp.append(f'{item[0][1:]} {item[1][0: 5]}')
                if len(temp) > 1:
                    event_value += 1
                    if temp[-2] != temp[-1]:
                        self.list_to_print.append(f'[{temp[-2]}] {event_value}')
                        event_value = 0
        self.write_to()

    def write_to(self):
        with open(self.file_to_write, mode='w', encoding='utf8') as file:
            for line in self.list_to_print:
                file.write(line)
                file.write('\n')


LogPaser(file_to_read='events.txt', file_to_write='NOK_events_per_min.txt', event='NOK')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
