# -*- coding: utf-8 -*-

import os
import time

# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>


class Trades:

    def __init__(self, path, tickers, *args, **kwargs):
        self.tickers = tickers
        self.path = path
        self.sorted = {}
        self.temp = {}
        self.run()
        self.volatility_to_sorted()

    def run(self):
        pyth_path = os.path.normpath(self.path)
        for dirpath, dirnames, filenames in os.walk(pyth_path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                with open(file_path, 'r', encoding='utf8') as trades_data:
                    self.analyse_to_temp(trades_data)

    def analyse_to_temp(self, trades_data):
        count = 0
        for line in trades_data:
            stripped_line = line.strip('\n')
            secid, trdetime, price_, quantity = stripped_line.split(',')
            price = price_.split('.')[0]
            if secid == 'SECID':
                count = len(self.temp) + 1
                continue
            if len(self.temp) != count:
                self.temp[f'{secid}'] = {'max': int(price), 'min': int(price)}
            else:
                if int(price) > self.temp[f'{secid}']['max']:
                    self.temp[f'{secid}']['max'] = int(price)
                elif int(price) < int(self.temp[f'{secid}']['min']):
                    self.temp[f'{secid}']['min'] = int(price)

    def volatility_to_sorted(self):
        time.sleep(1)
        for secid, prices in self.temp.items():
            max_price, min_price = prices['max'], prices['min']
            if max_price == 0 and min_price == 0:
                self.sorted[secid] = 0
            else:
                average_price = (max_price + min_price) / 2
                volatility = ((max_price - min_price) / average_price) * 100
                self.sorted[secid] = round(volatility, 2)
        self.max_volatility(tickers=self.tickers)
        self.min_volatility(tickers=self.tickers)
        self.zero_volatility()

    def max_volatility(self, tickers):
        print_count = 0
        print(f"{'Максимальная волатильность:': ^35}")
        for secid, volatility in reversed(sorted(self.sorted.items(), key=lambda item: item[1])):
            if volatility != 0 and print_count < tickers:
                print_count += 1
                print(f"{f'ТИКЕР {secid} - {volatility} %': ^35}")

    def min_volatility(self, tickers):
        print_count = 0
        print(f"{'Минимальная волатильность:': ^35}")
        for secid, volatility in list(sorted(self.sorted.items(), key=lambda item: item[1])):
            if volatility != 0 and print_count < tickers:
                print_count += 1
                print(f"{f'ТИКЕР {secid} - {volatility} %': ^35}")

    def zero_volatility(self):
        print(f"{'Нулевая волатильность:': ^35}")
        for secid, volatility in sorted(self.sorted.items()):
            if volatility == 0:
                print(f'ТИКЕР {secid}, ', end='')


path = 'D:\\m\\mvs\\pyp\\lesson_012\\trades\\'
test = Trades(path, 3)
