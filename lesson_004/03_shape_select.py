# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
figure_angles = {'треугольник': 120, 'квадрат': 90, 'пятиугольник': 72, 'шестиугольник': 60}
values_list = list(figure_angles.keys())


def figures_function(dictionary):
    print('Возможные фигуры:')
    for i, item in enumerate(dictionary):
        print('   ', i, ':', item)


def figure(name='квадрат', point=sd.get_point(150, 150), angle=0, length=200, width=2):
    if angle > 400:
        return
    side = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    side.draw()
    next_point = side.end_point
    next_angle = angle + figure_angles[name]
    figure(name=name, point=next_point, angle=next_angle, length=length,  width=width)


figures_function(figure_angles)
user_input = input('Введите желаемую фигуру:')
while not int(user_input.isnumeric()):
    print('Вы ввели некорректный номер!')
    user_input = input('Введите желаемую фигуру:')
    pass
while int(user_input) >= 4 or int(user_input) < 0:
    print('Вы ввели некорректный номер!')
    user_input = input('Введите желаемую фигуру:')
else:
    figure(name=values_list[int(user_input)])

sd.pause()
