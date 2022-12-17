# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

import simple_draw as sd


# def triangle(point=sd.get_point(350, 350), angle=0, length=200, width=2):
#     if angle > 361:
#         return
#     side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     side.draw()
#     next_point = side.end_point
#     next_angle = angle + 120
#     triangle(point=next_point, angle=next_angle, length=length, width=width)
#
#
# triangle(point=sd.get_point(400, 350), angle=50)
#
#
# def square(point=sd.get_point(350, 350), angle=0, length=200, width=2):
#     if angle > 361:
#         return
#     side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     side.draw()
#     next_point = side.end_point
#     next_angle = angle + 90
#     square(point=next_point, angle=next_angle, length=length,  width=width)
#
#
# square(point=sd.get_point(100, 450), angle=35, length=70)
#
#
# def octagon(point=sd.get_point(350, 350), angle=0, length=200, width=2):
#     if angle > 400:
#         return
#     side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     side.draw()
#     next_point = side.end_point
#     next_angle = angle + 72
#     octagon(point=next_point, angle=next_angle, length=length,  width=width)
#
#
# octagon(point=sd.get_point(220, 210), angle=90, length=95)
#
#
# def hexagon(point=sd.get_point(350, 350), angle=0, length=200, width=2):
#     if angle > 400:
#         return
#     side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     side.draw()
#     next_point = side.end_point
#     next_angle = angle + 60
#     hexagon(point=next_point, angle=next_angle, length=length,  width=width)
#
#
# hexagon(point=sd.get_point(420, 110), angle=40, length=85)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?


# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.


def figure(name='квадрат', point=sd.get_point(350, 350), angle=0, length=200, width=2):
    figure_angles = {'треугольник': 120, 'квадрат': 90, 'пятиугольник': 72, 'шестиугольник': 60}
    if angle > 400:
        return
    side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    side.draw()
    next_point = side.end_point
    next_angle = angle + figure_angles[name]
    figure(name=name, point=next_point, angle=next_angle, length=length,  width=width)


figure(name='треугольник')

# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
