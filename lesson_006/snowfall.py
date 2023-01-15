# -*- coding: utf-8 -*-

import simple_draw as sd
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
N = 20
count = 0
step = 0
x_list = []
y_list = []
rays_length_list = []
factor_a_list = []
factor_b_list = []
factor_c_list = []
wind_list = []


def create_snowflakes(N):
    for _ in range(N + 1):
        x_list.append(sd.random_number(a=7, b=593))
        y_list.append(sd.random_number(a=650, b=700))
        rays_length_list.append(sd.random_number(a=8, b=17))
        factor_a_list.append((sd.random_number(a=1, b=10) / 10))
        factor_b_list.append((sd.random_number(a=1, b=100) / 100))
        factor_c_list.append(sd.random_number(a=1, b=179))
        wind_list.append(sd.random_number(a=-20, b=20))


def create_colored_snowflakes(i, color):
    factor_a, factor_b, factor_c = factor_a_list[i], factor_b_list[i], factor_c_list[i]
    sd.snowflake(center=sd.get_point(x=x_list[i], y=y_list[i]), length=rays_length_list[i], color=color,
                 factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)


def snowflakes_moving(i):
    y_list[i] -= 50
    x_list[i] += wind_list[i]


def falling_snowflakes_numbers(i):
    if y_list[i] < -50:
        return True


def snowflakes_del(i):
    create_colored_snowflakes(i=i, color=sd.background_color)
    del y_list[i], x_list[i], rays_length_list[i], wind_list[i]
    del factor_a_list[i], factor_b_list[i], factor_c_list[i]


def create_new_snowflake(i):
    new_y = sd.random_number(a=650, b=700)
    nex_x = sd.random_number(a=5, b=595)
    new_length = sd.random_number(a=10, b=15)
    new_factor_a = (sd.random_number(a=1, b=10) / 10)
    new_factor_b = (sd.random_number(a=1, b=100) / 100)
    new_factor_c = sd.random_number(a=1, b=179)
    new_wind = sd.random_number(a=-20, b=20)
    y_list.insert(i, new_y), x_list.insert(i, nex_x), rays_length_list.insert(i, new_length)
    factor_a_list.insert(i, new_factor_a), factor_b_list.insert(i, new_factor_b), factor_c_list.insert(i, new_factor_c)
    wind_list.insert(i, new_wind)


# def snowflake(x):
#     for i in range(x):
#         sd.start_drawing()
#         point = sd.get_point(x=x_list[i], y=y_list[i])
#         length = rays_length_list[i]
#         factor_a, factor_b, factor_c = factor_a_list[i], factor_b_list[i], factor_c_list[i]
#         sd.snowflake(center=point, length=length, color=sd.background_color,
#                      factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
#         y_list[i] -= 35
#         x_list[i] += wind_list[sd.random_number(a=0, b=19)]
#         if y_list[i] < 45:
#             last_point = sd.get_point(x=x_list[i], y=snowdrift_list[i])
#             sd.snowflake(center=last_point, length=length, color=sd.COLOR_WHITE,
#                          factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
#             y_list[i] = sd.random_number(a=550, b=600)
#             x_list[i] = sd.random_number(a=10, b=590)
#             factor_a_list[i], factor_b_list[i], factor_c_list[i] = (sd.random_number(a=1, b=10) / 10),\
#                 (sd.random_number(a=1, b=100) / 100), (sd.random_number(a=1, b=179))
#             continue
#         new_point = sd.get_point(x=x_list[i], y=y_list[i])
#         sd.snowflake(center=new_point, length=length, color=sd.COLOR_WHITE,
#                      factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
#         sd.finish_drawing()
#         sd.sleep(0.1)

# sd.pause()