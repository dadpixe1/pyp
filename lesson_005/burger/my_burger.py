# -*- coding: utf-8 -*-

now = 'А теперь добавим'
bread = 'хлеб'
steak = 'котлету'
pickle = 'огурчик'
cheese = 'сыр'
tomato = 'помидор'
mayonnaise = 'майонез'

double_with_cheese_recipe = [bread, pickle, tomato, mayonnaise, cheese, steak, cheese, steak, bread]


def double_with_cheese(): # Вариант 1
    return reversed(double_with_cheese_recipe)

