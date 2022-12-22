# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
count = 0
N = 20
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
user_input = input('Укажите интенсивность снегопада (от 1 до 20): ')
x_list = []
y_list = []
rays_length_list = []
factor_a_list = []
factor_b_list = []
factor_c_list = []
wind_list = []
snowdrift_list = []


while count < N + N:
    count += 1
    x_list.append(sd.random_number(a=10, b=590))
    y_list.append(sd.random_number(a=550, b=600))
    rays_length_list.append(sd.random_number(a=10, b=15))
    factor_a_list.append((sd.random_number(a=1, b=10) / 10))
    factor_b_list.append((sd.random_number(a=1, b=100) / 100))
    factor_c_list.append(sd.random_number(a=1, b=179))
    wind_list.append(sd.random_number(a=-10, b=10))
    snowdrift_list.append(sd.random_number(a=15, b=45))


def snowflake(x):
    for i in range(x):
        sd.start_drawing()
        point = sd.get_point(x=x_list[i], y=y_list[i])
        length = rays_length_list[i]
        factor_a, factor_b, factor_c = factor_a_list[i], factor_b_list[i], factor_c_list[i]
        sd.snowflake(center=point, length=length, color=sd.background_color,
                     factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        y_list[i] -= 35
        x_list[i] += wind_list[sd.random_number(a=0, b=19)]
        if y_list[i] < 45:
            last_point = sd.get_point(x=x_list[i], y=snowdrift_list[i])
            sd.snowflake(center=last_point, length=length, color=sd.COLOR_WHITE,
                         factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
            y_list[i] = sd.random_number(a=550, b=600)
            x_list[i] = sd.random_number(a=10, b=590)
            factor_a_list[i], factor_b_list[i], factor_c_list[i] = (sd.random_number(a=1, b=10) / 10),\
                (sd.random_number(a=1, b=100) / 100), (sd.random_number(a=1, b=179))
            continue
        new_point = sd.get_point(x=x_list[i], y=y_list[i])
        sd.snowflake(center=new_point, length=length, color=sd.COLOR_WHITE,
                     factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        sd.finish_drawing()
        sd.sleep(0.1)


while True:
    for _ in range(int(user_input) + 1):
        snowflake(x=_)
    if sd.user_want_exit():
        break


while True:
    sd.clear_screen()
    pass
    pass
    pass
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


