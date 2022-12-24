# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    point = sd.get_point(x, y)
    left_eye = sd.get_point(x - 25, y + 20)
    right_eye = sd.get_point(x + 25, y + 20)
    sd.circle(center_position=point, radius=60, color=color, width=2)
    list_of_dots = sd.get_point(x - 30, y - 20), sd.get_point(x - 15, y - 30), \
                   sd.get_point(x + 15, y - 30), sd.get_point(x + 30, y - 20)
    sd.lines(point_list=list_of_dots, color=color, closed=False, width=2)
    sd.circle(center_position=left_eye, radius=6, color=color, width=2)
    sd.circle(center_position=right_eye, radius=6, color=color, width=2)


# for _ in range(10):
#     x = sd.random_number(a=0, b=600)
#     y = sd.random_number(a=0, b=600)
#     color = sd.random_color()
#     smile(x, y, color)


sd.pause()

