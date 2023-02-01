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
    """ period - event frequency: 'minute', 'hour', 'day', 'month' or 'year',
        event - data to find in log: 'your_data',
        file_to_read - your file name and file extension (can read .zip),
        file_to_write - name and extension of your output log file (file created automatically).
    """

    def __init__(self, file_to_read, file_to_write, event, period):
        self.method = period
        self.event = event
        self.file_to_write = file_to_write
        self.file_name = file_to_read
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
        self.method_choose()

    def method_choose(self):
        if self.method == 'minute':
            self.event_extracting(clock=5, calendar=None)
        elif self.method == 'hour':
            self.event_extracting(clock=2, calendar=None)
        elif self.method == 'day':
            self.event_extracting(clock=5, calendar=None)
        elif self.method == 'month':
            self.event_extracting(clock=5, calendar=-3)
        elif self.method == 'year':
            self.event_extracting(clock=5, calendar=-6)
        else:
            print('Error. You must choose correct period.')

    def event_extracting(self, clock, calendar):
        temp, last_line, event_value = [], 0, 0
        for line in self.log_list:
            if line == self.log_list[-2]:
                last_line = 1
            if self.event in line:
                item = line.split(' ')
                data, time = item[0][1:calendar:], item[1][0: clock]
                if self.method == 'minute' or self.method == 'hour':
                    temp.append(f'{data} {time}')
                else:
                    temp.append(f'{data}')
                if len(temp) > 1:
                    event_value += 1
                    if last_line == 1 and self.method == 'month' or last_line == 1 and self.method == 'year':
                        self.list_to_print.append(f'[{temp[-2]}] {event_value + 1}')
                    elif temp[-2] != temp[-1]:
                        self.list_to_print.append(f'[{temp[-2]}] {event_value}')
                        event_value = 0
        pprint(self.list_to_print)
        self.write_to()

    def write_to(self):
        with open(self.file_to_write, mode='w', encoding='utf8') as file:
            for line in self.list_to_print:
                file.write(line)
                file.write('\n')


LogPaser(file_to_read='events.txt', file_to_write='', event='NOK', period='minute')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
