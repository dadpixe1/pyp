# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
step = 0
brick_width, brick_length = 100, 50
sd.background_color = (127, 0, 0)


def element(x_1, y_1, x_2, y_2):
    """Исходные параметры кирпича"""
    start_of_brick, end_of_brick = sd.get_point(0 + x_1, 0 + y_1), sd.get_point(0 + x_2, 0 + y_2)
    sd.line(start_of_brick, end_of_brick, color=sd.COLOR_DARK_CYAN, width=3)


def one_row(symbol_1, symbol_2):
    """Нечетный ряд кирпичей"""
    element(x_1=step * 2, y_1=brick_width * symbol_1,
            x_2=step * 2, y_2=brick_length + brick_width * symbol_2)


def another_row(symbol_1, symbol_2):
    """Четный ряд кирпичей"""
    element(x_1=(step * 2) - brick_length, y_1=(brick_width * symbol_1) - brick_length,
            x_2=(step * 2) - brick_length, y_2=brick_width * symbol_2)



for horizontal_line in range(12):
    row_step = 0
    step += 50
    beginning_of_line, end_of_line = sd.get_point(0, 0 + step), sd.get_point(600, 0 + step)
    sd.line(beginning_of_line, end_of_line, color=sd.COLOR_DARK_CYAN, width=3)
    # Создание горизонтальных линий для укладки кирпича
    for bricks_row in range(7):
        one_row(row_step, row_step)
        another_row(row_step, row_step)
        row_step += 1
    # Укладка кирпича рядами



sd.pause()
