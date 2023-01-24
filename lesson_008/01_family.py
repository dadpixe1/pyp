# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

# Часть первая.
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.


class House:
    bedside_money = 100
    food_in_the_fridge = 50
    dirt = 0

    def __init__(self, name):
        self.name = name
        pass

    def __str__(self):
        return 'Денег в тумбочке - {}, еды в холодильнике - {}, грязи в {} - {}.'.format(
            self.bedside_money, self.food_in_the_fridge, self.name, self.dirt)


class Man:
    fullness = 30
    happiness = 100

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Я - {}, степень сытости - {}, счастье - {}.'.format(self.name, self.fullness, self.happiness)

    def act(self):
        home.dirt += 2.5
        if self.fullness < 0:
            print('Сытость - {}, {} - умер от голода.'.format(self.fullness, self.name))

    def eat(self):
        if home.food_in_the_fridge < 30:
            rest_of_food = home.food_in_the_fridge
            self.fullness += rest_of_food
            home.food_in_the_fridge -= rest_of_food
        else:
            self.fullness += 30
            home.food_in_the_fridge -= 30


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        super().eat()
        pass

    def work(self):
        self.fullness -= 10
        home.bedside_money += 150

    def gaming(self):
        self.fullness -= 10
        pass


class Wife(Man):
    fur_coats = 0

    def __init__(self, name):
        super().__init__(name=name)
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        super().eat()
        pass

    def shopping(self):
        if home.bedside_money == 0:
            print('Дожили, нет денег купить еды.')
            self.fullness -= 10
        elif home.bedside_money <= 70:
            rest_of_money = home.bedside_money
            home.bedside_money -= rest_of_money
            home.food_in_the_fridge += rest_of_money
            self.fullness -= 10
        else:
            home.bedside_money -= 70
            home.food_in_the_fridge += 70
            self.fullness -= 10

    def buy_fur_coat(self):
        if home.bedside_money >= 350:
            self.fullness -= 10
            self.fur_coats += 1
            home.bedside_money -= 350

    def clean_house(self):
        self.fullness -= 10
        pass
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,

home = House(name='Хоум')
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    print('================== День {} =================='.format(day))
    serge.act()
    masha.act()
    print(serge)
    print(masha)
    print(home)

# TODO после реализации первой части - отдать на проверку учителю

# Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


# Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


# Часть третья
#
# после подтверждения учителем второй части (обеих веток).
# Влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживания случайностей моделирование за год делать 3 раза, если 2 из 3-х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

