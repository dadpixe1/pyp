# -*- coding: utf-8 -*-

import os
import time
from pprint import pprint
from threading import Thread
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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


class Trades(Thread):

    def __init__(self, name, path, statistic, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.path = path
        self.sorted = statistic
        self.temp = {}

    def run(self):
        pyth_path = os.path.normpath(self.path)
        for dirpath, dirnames, filenames in os.walk(pyth_path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                with open(file_path, 'r', encoding='utf8') as trades_data:
                    self.analyse_to_temp(trades_data)

    def analyse_to_temp(self, trades_data):
        count = 0
        time.sleep(0.0000001)
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
        self.volatility_to_sorted()

    def volatility_to_sorted(self):
        for secid, prices in self.temp.items():
            max_price, min_price = prices['max'], prices['min']
            if max_price == 0 and min_price == 0:
                self.sorted[secid] = 0
            else:
                average_price = (max_price + min_price) / 2
                volatility = ((max_price - min_price) / average_price) * 100
                self.sorted[secid] = round(volatility, 2)


class TradesTickersStat:

    def __init__(self, tickers, dict):
        self.tickers = tickers
        self.sorted = dict
        self.max_volatility(tickers)
        self.min_volatility(tickers)
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
statistic = {}
# trades = [Trades(name=str(name), path=path, tickers=3, barrier=barrier) for name in range(2)]
# for trade in trades:
#     trade.start()
# for trade in trades:
#     trade.join()
a = Trades(name='a', path=path, statistic=statistic)
b = Trades(name='b', path=path, statistic=statistic)

a.start()
b.start()

a.join()
b.join()

TradesTickersStat(tickers=3, dict=statistic)
