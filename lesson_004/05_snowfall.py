# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
random_start_points_x = []
count = 0
snowflakes_count = 0
y = 500
length = sd.random_number(a=50, b=100)


def snowflake_falling(x, y, length):
    while True:
        sd.clear_screen()
        point = sd.get_point(x=x, y=y)
        sd.snowflake(center=point, length=length)
        y -= 10
        if y < 50:
            break
        x += 10
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
#     # point2 = sd.get_point(x2, y2)
#     # sd.snowflake(center=point2, length=30)
#     # y2 -= 10
#     # if y2 < 50:
#     #    break
#     # x2 = x2 + 20


while count < N:
    count += 1
    if count > 21:
        break
    random_start_points_x.append(sd.random_number(a=50, b=550))


while snowflakes_count < N:
    snowflakes_count += 1
    if snowflakes_count > 21:
        break
    new_x = random_start_points_x[snowflakes_count]
    snowflake_falling(x=new_x, y=y, length=length)


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


