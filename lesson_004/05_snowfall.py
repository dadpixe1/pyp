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
x_list = []
y_list = []
rays_length_list = []
wind = sd.random_number(a=2, b=10)


while count < N + 1:
    count += 1
    x_list.append(sd.random_number(a=10, b=590))
    y_list.append(sd.random_number(a=550, b=600))
    rays_length_list.append(sd.random_number(a=10, b=30))


def hz(x):
    for i in range(x):
        sd.start_drawing()
        point = sd.get_point(x=x_list[i], y=y_list[i])
        length = rays_length_list[i]
        sd.snowflake(center=point, length=length, color=sd.background_color)
        y_list[i] -= 40
        x_list[i] += sd.random_number(a=-2, b=6)

            # sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
        new_point = sd.get_point(x=x_list[i], y=y_list[i])
        sd.snowflake(center=new_point, length=length, color=sd.COLOR_WHITE)
        if y_list[0] < 25:
            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
            continue
        sd.finish_drawing()
        sd.sleep(0.1)


while True:
    for _ in range(N + 1):
        hz(x=_)
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


