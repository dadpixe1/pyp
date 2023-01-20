# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} Вьехал в дом'.format(self.name))

    def eat(self):
        if self.house.cat_food <= 10:
            print('{} Нет еды'.format(self.name))
        else:
            print('{} сытно поел'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 20

    def sleep(self):
        print('{} сладко поспал'.format(self.name))
        self.fullness -= 10

    def wallpaper_scratching(self):
        print('{} пустил обои на макароны'.format(self.name))
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            print('{} сдох'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.wallpaper_scratching()
        elif dice == 2:
            self.wallpaper_scratching()
        else:
            self.sleep()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.knowledge = 0
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        print('{} поел'.format(self.name))
        self.fullness += 10
        self.house.food -= 10

    def work(self):
        if self.knowledge >= 50:
            print('{} сходил на новую работу'.format(self.name))
            self.house.money += 100
            self.fullness -= 10
        else:
            print('{} сходил на работу'.format(self.name))
            self.house.money += 50
            self.fullness -= 10

    def get_cat(self):
        kittie.go_to_the_house(house=my_sweet_home)

    def buy_cat_food(self):
        if self.house.cat_food <= 10:
            print('{} купил кошачей еды'.format(self.name))
            self.house.cat_food += 50
            self.house.money -= 50
        else:
            self.eat()

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            self.work()

    def study_python(self):
        print('{} учился компуктеру'.format(self.name))
        self.house.money -= 100
        self.fullness -= 10
        self.knowledge += 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} Вьехал в дом'.format(self.name))

    def clean_flat(self):
        self.house.dirt -= 13
        self.fullness -= 20
        print('{} Убрал за шерстяным'.format(self.name))

    def act(self):
        if kittie.house is None:
            self.get_cat()
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif kittie.fullness <= 10:
            self.buy_cat_food()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.money > 150:
            self.study_python()
        elif self.knowledge == 50:
            print('{} устроился компутерщиком'.format(self.name))
            self.knowledge += 5
        elif dice == 1:
            self.clean_flat()
        elif dice == range(2, 6):
            self.eat()
        else:
            if self.fullness > 50:
                self.work()
            else:
                self.eat()

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В холодильнике еды осталось {}, денег в тумбочке осталось {}, еды у кота {}, грязи в доме {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


man = Man(name='Хлодвиг')
kittie = Cat(name='Башмак')


my_sweet_home = House()
man.go_to_the_house(my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    man.act()
    kittie.act()
    print('--- в конце дня ---')
    print(man)
    print(kittie)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
