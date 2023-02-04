# -*- coding: utf-8 -*-

from random import randint

# День сурка.
#
# Напишите функцию one_day(), которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день.
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):

    def __init__(self, carma, message='Phil spoke a lot'):
        self.message = message
        self.carma = carma
        super().__init__(self.message)

    def __str__(self):
        return f'До стерилизации Фила еще {ENLIGHTENMENT_CARMA_LEVEL - self.carma} кармы,' \
               f' сегодня кармы не будет: {self.message}.'


class DrunkError(Exception):

    def __init__(self, carma, message='Phil boozed'):
        self.message = message
        self.carma = carma
        super().__init__(self.message)

    def __str__(self):
        return f'До стерилизации Фила еще {ENLIGHTENMENT_CARMA_LEVEL - self.carma} кармы,' \
               f' сегодня кармы не будет: {self.message}.'


class CarCrashError(Exception):

    def __init__(self, carma, message='Phil drove not carefully'):
        self.message = message
        self.carma = carma
        super().__init__(self.message)

    def __str__(self):
        return f'До стерилизации Фила еще {ENLIGHTENMENT_CARMA_LEVEL - self.carma} кармы,' \
               f' сегодня кармы не будет: {self.message}.'


class GluttonyError(Exception):

    def __init__(self, carma, message='Phil eat 60 cream pies'):
        self.message = message
        self.carma = carma
        super().__init__(self.message)

    def __str__(self):
        return f'До стерилизации Фила еще {ENLIGHTENMENT_CARMA_LEVEL - self.carma} кармы,' \
               f' сегодня кармы не будет: {self.message}.'


class DepressionError(Exception):

    def __init__(self, carma, message='Phil stay in bed all day long'):
        self.message = message
        self.carma = carma
        super().__init__(self.message)

    def __str__(self):
        return f'До стерилизации Фила еще {ENLIGHTENMENT_CARMA_LEVEL - self.carma} кармы,' \
               f' сегодня кармы не будет: {self.message}.'


class SuicideError(Exception):

    def __init__(self, carma, message='Phil done it again'):
        self.message = message
        self.carma = carma
        super().__init__(self.message)

    def __str__(self):
        return f'До стерилизации Фила еще {ENLIGHTENMENT_CARMA_LEVEL - self.carma} кармы,' \
               f' сегодня кармы не будет: {self.message}.'


def oneday(*args):
    dice, phil_connors_errors = randint(1, 13), 100
    if dice == 1:
        phil_connors_errors = randint(1, 78)
    if phil_connors_errors <= 13:
        raise IamGodError(carma=total)
    elif 13 < phil_connors_errors <= 26:
        raise DrunkError(carma=total)
    elif 26 < phil_connors_errors <= 39:
        raise CarCrashError(carma=total)
    elif 39 < phil_connors_errors <= 52:
        raise GluttonyError(carma=total)
    elif 52 < phil_connors_errors <= 65:
        raise DepressionError(carma=total)
    elif 65 < phil_connors_errors <= 78:
        raise SuicideError(carma=total)
    else:
        carma = randint(1, 7)
    return carma


total, day = 0, 0
with open('groundhog_log.txt', mode='w', encoding='utf8') as file:
    while total < ENLIGHTENMENT_CARMA_LEVEL:
        day += 1
        try:
            total += oneday(total)
        except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
            file.write(f'# День {day}, ошибка Фила - {type(exc)}, карма Фила - {total}\n# {exc}')
            file.write('\n')
            print(f'Фил пойман с поличным на {type(exc)}, карма - {total}\n{exc}\n{day:=^90}')
print(f'Карма - {total}, закончили упражнение за {day} дней.')

# https://goo.gl/JnsDqu
