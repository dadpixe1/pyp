# -*- coding: utf-8 -*-

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
    accounting = 0
    food_in_the_fridge = 50
    cat_food = 30
    food_accounting = 0
    dirt = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        self.dirt += 5
        return 'Денег в тумбочке - {}, еды в холодильнике - {}, грязи в {} - {}.'.format(
            self.bedside_money, self.food_in_the_fridge, self.name, self.dirt)


class Man:
    fullness = 30
    happiness = 100
    sex_grammar = ''

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Я - {}, степень сытости - {}, счастье - {}.'.format(self.name, self.fullness, self.happiness)

    def buy_cat_food(self):
        dice = randint(5, 10)
        home.cat_food += dice
        home.bedside_money -= dice
        print('{} купил{} {} {} еды.'.format(self.name, self.sex_grammar, Cat.__name__, dice))

    def act(self):
        cat_petting_dice = randint(1, 25)
        if home.dirt > 90:
            self.happiness -= 10
            return True
        if self.fullness < 0:
            print('Сытость - {}, {} - умер от голода.'.format(self.fullness, self.name))
            return False
        if self.happiness < 10:
            print('Счастья - {}, {} - умер от депрессии.'.format(self.happiness, self.name))
            return False
        if home.cat_food < 10:
            self.buy_cat_food()
            self.fullness -= 10
            return False
        if cat_petting_dice == 1:
            self.fullness -= 10
            self.happiness += 5
            print('{} гладит шерстяного.'.format(self.name))
            return False
        return True

    def eat(self):
        food_to_eat = randint(1, 30)
        if home.food_in_the_fridge == 0:
            self.fullness -= 10
            print('Еды в холодильнике нет.')
        elif home.food_in_the_fridge < food_to_eat:
            rest_of_food = home.food_in_the_fridge
            home.accounting += rest_of_food
            self.fullness += rest_of_food
            home.food_in_the_fridge -= rest_of_food
            print('{} поел{} {} еды.'.format(self.name, self.sex_grammar, rest_of_food))
        else:
            home.food_accounting += food_to_eat
            self.fullness += food_to_eat
            home.food_in_the_fridge -= food_to_eat
            print('{} поел{} {} еды.'.format(self.name, self.sex_grammar, food_to_eat))


class Husband(Man):
    salary = 150

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            if self.fullness <= 26:
                self.eat()
            elif home.bedside_money <= 70:
                self.work()
            else:
                self.gaming()

    def eat(self, sex_grammar=None):
        super().eat()

    def work(self):
        self.fullness -= 10
        self.happiness -= 10
        home.bedside_money += self.salary
        print('{} сходил на работу. Положил в тумбочку {}.'.format(self.name, self.salary))

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        print('{} игрался в игры.'.format(self.name))


class Wife(Man):
    fur_coats = 0
    sex_grammar = 'а'

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            if self.fullness <= 26:
                self.eat()
            elif home.food_in_the_fridge <= 60:
                self.shopping()
            elif home.dirt > 15:
                self.clean_house()
            else:
                self.buy_fur_coat()

    def eat(self):
        super().eat()

    def shopping(self):
        value_of_purchase = randint(50, 75)
        if home.bedside_money == 0:
            self.fullness -= 10
            print('Дожили, нет денег купить еды.')
        elif home.bedside_money <= value_of_purchase:
            self.fullness -= 10
            rest_of_money = home.bedside_money
            home.accounting += rest_of_money
            home.bedside_money -= rest_of_money
            home.food_in_the_fridge += rest_of_money
            print('{} купила {} еды на остатки денег.'.format(self.name, rest_of_money))
        else:
            self.fullness -= 10
            home.accounting += value_of_purchase
            home.bedside_money -= value_of_purchase
            home.food_in_the_fridge += value_of_purchase
            print('{} купила {} еды.'.format(self.name, value_of_purchase))

    def buy_fur_coat(self):
        fur_coat_cost = 350
        if home.bedside_money >= fur_coat_cost:
            self.fullness -= 10
            self.fur_coats += 1
            self.happiness += 60
            home.accounting += fur_coat_cost
            home.bedside_money -= fur_coat_cost
            print('{} купила шубу.'.format(self.name))
        else:
            self.fullness -= 10
            print('{} жалуется, что на шубу не хватает {} денег.'.format(self.name, fur_coat_cost - home.bedside_money))

    def clean_house(self):
        value_of_cleaning = randint(1, 100)
        self.fullness -= 10
        home.dirt -= value_of_cleaning
        print('{} убралась в доме, грязи стало меньше на {}.'.format(self.name, value_of_cleaning))


home = House(name='Хаус')
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

# for day in range(1, 366):
#     print('================== День {} =================='.format(day))
#     serge.act()
#     masha.act()
#     print(serge)
#     print(masha)
#     print(home)
# print('=========== Итоги союза {} и {} ==========='.format(serge.name, masha.name))
# print('Всего денег потрачено - {}, еды съедено - {}, шуб куплено - {}.'.format(
#     home.accounting, home.food_accounting, masha.fur_coats))

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
    fullness = 30
    cat_alive = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Я - кот {}, сытость - {}.'.format(self.name, self.fullness)

    def act(self):
        dice = randint(1, 10)
        if self.cat_alive == 1:
            print('{} больше не с нами.'.format(self.name))
        if self.fullness < 10:
            self.eat()
        elif dice > 8:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        if self.fullness < 0:
            self.cat_alive = 1
            print('{} издох.'.format(self.name))
            return '{} больше не с нами.'.format(self.name)
        else:
            dice = randint(7, 10)
            self.fullness += dice * 2
            home.cat_food -= dice
            print('{} поел {} еды.'.format(self.name, dice))

    def sleep(self):
        self.fullness -= 10
        print('{} поспал.'.format(self.name))

    def soil(self):
        self.fullness -= 10
        home.dirt += 5
        print('{} драл обои.'.format(self.name))


cat = Cat(name='Пират')

for day in range(1, 366):
    print('================== День {} =================='.format(day))
    serge.act()
    masha.act()
    cat.act()
    print(serge)
    print(masha)
    print(cat)
    print(home)
print('=========== Итоги союза {} и {} ==========='.format(serge.name, masha.name))
print('Всего денег потрачено - {}, еды съедено - {}, шуб куплено - {}.'.format(
    home.accounting, home.food_accounting, masha.fur_coats))
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

