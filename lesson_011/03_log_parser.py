# -*- coding: utf-8 -*-

from pprint import pprint
import zipfile
# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def log_collect(file_name):
    log, count = [], 0
    with open(file_name, 'r', encoding='cp1251') as file:
        for line in file:
            if 'NOK' in line:
                item = line.split(' ')
                data, time = item[0][1::], item[1][0: 5]
                log.append(f'{data} {time}')
                if len(log) > 1:
                    count += 1
                    if log[-2] != log[-1]:
                        yield log[-2], count
                        count = 0


grouped_events = log_collect('events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

