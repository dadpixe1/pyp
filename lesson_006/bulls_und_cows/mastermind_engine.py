# -*- coding: utf-8 -*-
from random import randint
_holder = []
count = 0
bulls_cows_dict = {'bulls': 0, 'cows': 0}


def number_choose():
    if len(_holder) == 4:
        del _holder[:]
    _holder.append(randint(a=1, b=9))
    while len(_holder) < 4:
        number = randint(a=0, b=9)
        if number not in _holder:
            _holder.append(number)


def number_guess(user_input, bulls, cows):
    bulls_cows_dict['bulls'], bulls_cows_dict['cows'] = 0, 0
    for i in user_input:
        if int(i) not in _holder:
            pass
        elif user_input.index(i) == _holder.index(int(i)):
            bulls += 1
            bulls_cows_dict['bulls'] = bulls
        else:
            cows += 1
            bulls_cows_dict['cows'] = cows
    return bulls_cows_dict

