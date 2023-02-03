# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

# BRUCE_WILLIS = 42
#
# input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
# leeloo = int(input_data[4])
# result = BRUCE_WILLIS * leeloo
# print(f"- Leeloo Dallas! Multi-pass № {result}!")

# Обернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соответствующее сообщение.


try:
    BRUCE_WILLIS = 42

    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
except ValueError as exc:
    print(f'{type(exc)} - невозможно преобразовать к числу')
except IndexError as exc:
    print(f'{type(exc)} - выход за границы списка')
except BaseException as exc:
    print(f'{type(exc)} - это что-то новое')
else:
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
