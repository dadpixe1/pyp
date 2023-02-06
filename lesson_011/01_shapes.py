# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def figure(point=sd.get_point(350, 350), angle=0, length=200):
        sides = list(range(3, 12))
        if angle > 361:
            return
        value = [360 / x for x in sides if x == n]
        side = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        side.draw()
        next_point = side.end_point
        next_angle = angle + value[0]
        return figure(point=next_point, angle=next_angle, length=length)
    return figure


draw_triangle = get_polygon(n=2)
draw_triangle(point=sd.get_point(200, 200), angle=33, length=50)


sd.pause()
