# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
colors_list = {'red': (255, 0, 0), 'orange': (255, 127, 0), 'yellow': (255, 255, 0),
               'green': (0, 255, 0), 'cyan': (0, 255, 255), 'blue': (0, 0, 255), 'purple': (255, 0, 255)}
values_list = list(colors_list.values())


def colors_function(dictionary):
    print('Возможные цвета:')
    for i, item in enumerate(dictionary):
        print('   ', i, ':', item)


colors_function(colors_list)
user_input = input('Введите желаемый цвет:')
color = values_list[int(user_input)]


def triangle(point=sd.get_point(350, 200), angle=0, length=200, width=2, color=color):
    if angle > 361:
        return
    side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    side.draw(color=color)
    next_point = side.end_point
    next_angle = angle + 120
    triangle(point=next_point, angle=next_angle, length=length, width=width, color=color)


triangle(point=sd.get_point(400, 350), angle=50)


def square(point=sd.get_point(350, 350), angle=0, length=200, width=2, color=color):
    if angle > 361:
        return
    side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    side.draw(color=color)
    next_point = side.end_point
    next_angle = angle + 90
    square(point=next_point, angle=next_angle, length=length,  width=width, color=color)


square(point=sd.get_point(100, 450), angle=35, length=70)


def octagon(point=sd.get_point(350, 350), angle=0, length=200, width=2, color=color):
    if angle > 400:
        return
    side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    side.draw(color=color)
    next_point = side.end_point
    next_angle = angle + 72
    octagon(point=next_point, angle=next_angle, length=length,  width=width, color=color)


octagon(point=sd.get_point(220, 210), angle=90, length=95)


def hexagon(point=sd.get_point(350, 350), angle=0, length=200, width=2, color=color):
    if angle > 400:
        return
    side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    side.draw(color=color)
    next_point = side.end_point
    next_angle = angle + 60
    hexagon(point=next_point, angle=next_angle, length=length,  width=width, color=color)


hexagon(point=sd.get_point(420, 110), angle=40, length=85)

sd.pause()
