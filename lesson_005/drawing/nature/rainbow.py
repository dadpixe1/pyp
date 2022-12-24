# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
step = 0

# for color in rainbow_colors:
#    step += 5
#    beginning_of_line, end_of_line = sd.get_point(50 + step, 50), sd.get_point(350 + step, 450)
#    sd.line(beginning_of_line, end_of_line, color, 4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(300, -80)
radius = 150
width = 22
radius_step = 23


def rainbow(radius, radius_step, point, width):
    for color in rainbow_colors:
        radius += radius_step
        sd.circle(point, radius, color, width=width)



# rainbow(radius=radius, radius_step=radius_step, point=point, width=width)
sd.pause()
