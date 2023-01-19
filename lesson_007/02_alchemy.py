# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self):
        self.water = None

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return 'Шторм'
        elif isinstance(other, Fire):
            return 'Пар'
        elif isinstance(other, Time):
            return 'Роскошь'
        else:
            if isinstance(other, Earth):
                return 'Грязь'


class Air:

    def __init__(self):
        self.air = None

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'Шторм'
        elif isinstance(other, Fire):
            return 'Молния'
        elif isinstance(other, Time):
            return 'Дефицит'
        else:
            if isinstance(other, Earth):
                return 'Пыль'


class Fire:

    def __init__(self):
        self.fire = None

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'Пар'
        elif isinstance(other, Air):
            return 'Молния'
        elif isinstance(other, Time):
            return 'Угли'
        else:
            if isinstance(other, Earth):
                return 'Лава'


class Earth:

    def __init__(self):
        self.earth = None

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'Грязь'
        elif isinstance(other, Air):
            return 'Пыль'
        elif isinstance(other, Time):
            return 'Песок'
        else:
            if isinstance(other, Fire):
                return 'Лава'


class Time:

    def __init__(self):
        self.time = None

    def __str__(self):
        return 'Время'

    def __add__(self, other):
        if isinstance(other, Water):
            return 'Роскошь'
        elif isinstance(other, Air):
            return 'Дефицит'
        elif isinstance(other, Fire):
            return 'Угли'
        else:
            if isinstance(other, Earth):
                return 'Песок'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Time(), '+', Fire(), '=', Time() + Fire())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
