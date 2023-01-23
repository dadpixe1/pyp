# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


# class Snowflake:
#     pass
#
#     def __init__(self):
#         self.x = 280
#         self.y = 650
#         self.length = 30
#         self.draw_color = sd.COLOR_CYAN
#         self.remove_color = sd.background_color
#         self.factor_a = 0.5
#         self.factor_b = 0.1
#         self.factor_c = 90
#
#     def draw(self):
#         sd.snowflake(center=sd.get_point(x=self.x, y=self.y), length=self.length, color=self.draw_color,
#                      factor_a=self.factor_a, factor_b=self.factor_b, factor_c=self.factor_c)
#         sd.finish_drawing()
#         print(self.y)
#
#     def move(self):
#         self.y -= 25
#         self.x += 2
#
#     def clear_previous_picture(self):
#         sd.start_drawing()
#         sd.snowflake(center=sd.get_point(x=self.x, y=self.y), length=self.length, color=self.remove_color,
#                      factor_a=self.factor_a, factor_b=self.factor_b, factor_c=self.factor_c)
#
#     def can_fall(self):
#         if self.y < -50:
#             return True
#
#
# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

class Snowflake:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 30
        self.draw_color = sd.COLOR_CYAN
        self.remove_color = sd.background_color
        self.factor_a = 0.5
        self.factor_b = 0.1
        self.factor_c = 90

    def draw(self):
        sd.snowflake(center=sd.get_point(x=self.x, y=self.y), length=self.length, color=self.draw_color,
                     factor_a=self.factor_a, factor_b=self.factor_b, factor_c=self.factor_c)
        sd.finish_drawing()

    def move(self):
        self.y -= 25
        self.x += 2

    def clear_previous_picture(self):
        sd.start_drawing()
        sd.snowflake(center=sd.get_point(x=self.x, y=self.y), length=self.length, color=self.remove_color,
                     factor_a=self.factor_a, factor_b=self.factor_b, factor_c=self.factor_c)

    def can_fall(self):
        if self.y < -50:
            return True


N = 20


def get_flakes(count):
    flakes_list = []
    for _ in range(1, count):
        each_flake = Snowflake(x=(sd.random_number(a=5, b=595)), y=(sd.random_number(a=595, b=650)))
        flakes_list.append(each_flake)
    return flakes_list


def get_fallen_flakes():
    for i in range(1, len(flakes)):
        if flakes[i].y < -50:
            return i


def append_flakes(count):
    flakes[count].y = (sd.random_number(a=595, b=650))
    flakes[count].x = (sd.random_number(a=5, b=595))


flakes = get_flakes(count=N)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
