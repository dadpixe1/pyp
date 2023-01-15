# -*- coding: utf-8 -*-

import simple_draw as sd
from lesson_006.snowfall import create_snowflakes, create_colored_snowflakes, snowflakes_moving, \
    falling_snowflakes_numbers, snowflakes_del, create_new_snowflake, count, N, step
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


create_snowflakes(N=N)
while True:
    for i in range(count):
        sd.start_drawing()
        #  нарисовать_снежинки_цветом(color=sd.background_color)
        create_colored_snowflakes(i=i, color=sd.background_color)
        # сдвинуть_снежинки()
        snowflakes_moving(i=i)
        #  нарисовать_снежинки_цветом(color)
        create_colored_snowflakes(i=i, color=sd.COLOR_WHITE)
        # если есть номера_достигших_низа_экрана() то
        if falling_snowflakes_numbers(i=i) is True:
        #     удалить_снежинки(номера)
            snowflakes_del(i=i)
        #     создать_снежинки(count)
            create_new_snowflake(i=i)
        sd.sleep(0.1)
        sd.finish_drawing()
    step += 1
    if count < N and step % 5 == 0:
        count += 1
