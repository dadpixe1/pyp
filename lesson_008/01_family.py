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
        return 'Денег в тумбочке - {}, еды в холодильнике - {}, еды у котов - {}, грязи в {} - {}.'.format(
            self.bedside_money, self.food_in_the_fridge, self.cat_food, self.name, self.dirt)


class Man:
    fullness = 30
    happiness = 100
    sex_grammar = ''
    man_alive = True

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Я - {}, степень сытости - {}, счастье - {}.'.format(self.name, self.fullness, self.happiness)

    def buy_cat_food(self):
        purchase_amount = (Husband.salary / 15) + randint(10, 30)
        if home.bedside_money == 0:
            self.fullness -= 10
            # print('Денег на еду шерстяному нет.')
        elif home.bedside_money < purchase_amount:
            home.cat_food += home.bedside_money
            home.bedside_money -= home.bedside_money
            home.accounting -= home.bedside_money
            self.fullness -= 10
            # print('{} купил{} котам {} еды.'.format(self.name, self.sex_grammar, home.bedside_money))
        else:
            home.cat_food += purchase_amount
            home.bedside_money -= purchase_amount
            home.accounting += purchase_amount
            self.fullness -= 10
            # print('{} купил{} котам {} еды.'.format(self.name, self.sex_grammar, 50))

    def cat_petting(self):
        self.fullness -= 10
        self.happiness += 5
        # print('{} гладит шерстяного.'.format(self.name))

    def act(self):
        cat_petting_dice = randint(1, 60)
        if not self.man_alive:
            # print('{} больше не с нами.'.format(self.name))
            return False
        if self.fullness < 0:
            self.man_alive = False
            # print('Сытость - {}, {} - умер от голода.'.format(self.fullness, self.name))
            return False
        if self.happiness < 10:
            self.man_alive = False
            # print('Счастья - {}, {} - умер от депрессии.'.format(self.happiness, self.name))
            return False
        if cat_petting_dice == 3:
            self.cat_petting()
            return False
        return True

    def eat(self):
        # food_to_eat = randint(1, 30)
        if home.food_in_the_fridge == 0:
            self.fullness -= 10
            # print('Еды в холодильнике нет.')
        elif home.food_in_the_fridge < 30:
            rest_of_food = home.food_in_the_fridge
            home.accounting += rest_of_food
            self.fullness += rest_of_food
            home.food_in_the_fridge -= rest_of_food
            # print('{} поел{} {} еды.'.format(self.name, self.sex_grammar, rest_of_food))
        else:
            home.food_accounting += 30
            self.fullness += 30
            home.food_in_the_fridge -= 30
            # print('{} поел{} {} еды.'.format(self.name, self.sex_grammar, 30))


class Husband(Man):
    salary = 150

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 2)
        if home.dirt > 90:
            self.happiness -= 10
        if super().act():
            if self.fullness <= 28:
                self.eat()
            elif home.bedside_money <= 74:
                self.work()
            elif home.cat_food < 50:
                self.buy_cat_food()
            elif dice == 1:
                self.work()
            # elif dice == 2:
            #     self.buy_cat_food()
            else:
                self.gaming()

    def eat(self, sex_grammar=None):
        super().eat()

    def work(self):
        self.fullness -= 10
        self.happiness -= 10
        home.bedside_money += self.salary
        # print('{} сходил на работу. Положил в тумбочку {}.'.format(self.name, self.salary))

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        # print('{} игрался в игры.'.format(self.name))


class Wife(Man):
    fur_coats = 0
    sex_grammar = 'а'

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 6)
        if home.dirt > 90:
            self.happiness -= 10
        if super().act():
            if self.fullness <= 28:
                self.eat()
            elif home.food_in_the_fridge <= 62:
                self.shopping()
            elif home.dirt > 20:
                self.clean_house()
            elif home.cat_food < 50:
                self.buy_cat_food()
            elif dice == 3:
                self.buy_fur_coat()
            else:
                self.buy_cat_food()

    def eat(self):
        super().eat()

    def shopping(self):
        value_of_purchase = 100
        if home.bedside_money == 0:
            self.fullness -= 10
            # print('Дожили, нет денег купить еды.')
        elif home.bedside_money < value_of_purchase:
            self.fullness -= 10
            rest_of_money = home.bedside_money
            home.accounting += rest_of_money
            home.bedside_money -= rest_of_money
            home.food_in_the_fridge += rest_of_money
            # print('{} купила {} еды на остатки денег.'.format(self.name, rest_of_money))
        else:
            self.fullness -= 10
            home.accounting += value_of_purchase
            home.bedside_money -= value_of_purchase
            home.food_in_the_fridge += value_of_purchase
            # print('{} купила {} еды.'.format(self.name, value_of_purchase))

    def buy_fur_coat(self):
        fur_coat_cost = 350
        if home.bedside_money >= fur_coat_cost:
            self.fullness -= 10
            self.fur_coats += 1
            self.happiness += 60
            home.accounting += fur_coat_cost
            home.bedside_money -= fur_coat_cost
            # print('{} купила шубу.'.format(self.name))
        else:
            self.fullness -= 10
            # print('{} жалуется, что на шубу не хватает {} денег.'.format(
            # self.name, fur_coat_cost - home.bedside_money))

    def clean_house(self):
        value_of_cleaning = 100
        self.fullness -= 10
        home.dirt -= value_of_cleaning
        # print('{} убралась в доме, грязи стало меньше на {}.'.format(self.name, value_of_cleaning))


# home = House(name='Хаус')
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')

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
    cat_alive = True

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Я - кот {}, сытость - {}.'.format(self.name, self.fullness)

    def act(self):
        dice = randint(1, 10)
        if not self.cat_alive:
            # print('{} больше не с нами.'.format(self.name))
            pass
        elif self.fullness <= 0:
            self.cat_alive = False
            # print('{} больше не с нами.'.format(self.name))
            pass
        elif home.cat_food <= 0:
            self.fullness -= 10
            # print('У {}а закончилась еда.'.format(self.name))
        elif self.fullness < 30:
            self.eat()
        elif dice > 7:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        if self.fullness < 0:
            self.cat_alive = False
            # print('{} издох.'.format(self.name))
        else:
            dice = randint(1, 10)
            self.fullness += dice * 2
            home.cat_food -= dice
            # print('{} поел {} еды.'.format(self.name, dice))

    def sleep(self):
        self.fullness -= 10
        # print('{} поспал.'.format(self.name))

    def soil(self):
        self.fullness -= 10
        home.dirt += 5
        # print('{} драл обои.'.format(self.name))


# cat = Cat(name='Пират')
#
# for day in range(1, 366):
#     print('================== День {} =================='.format(day))
#     serge.act()
#     masha.act()
#     cat.act()
#     print(serge)
#     print(masha)
#     print(cat)
#     print(home)
# print('=========== Итоги союза {} и {} ==========='.format(serge.name, masha.name))
# print('Всего денег потрачено - {}, еды съедено - {}, шуб куплено - {}.'.format(
#     home.accounting, home.food_accounting, masha.fur_coats))
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

class Child(Man):
    happiness = 100
    fullness = 30

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if not self.man_alive:
            pass
            # print('{} больше не с нами.'.format(self.name))
        if self.fullness < 0:
            self.man_alive = False
            # print('{} - умер от голода.'.format(self.name))
        elif self.fullness <= 15:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        dice = randint(1, 10)
        if home.food_in_the_fridge <= 0:
            self.fullness -= 10
            # print('A-a-a-a-a-a-a-a-a-a-a-a')
        else:
            self.fullness += dice
            # print('{} поел.'.format(self.name))

    def sleep(self):
        self.fullness -= 10
        # print('{} поспал.'.format(self.name))


# Часть третья
#
# после подтверждения учителем второй части (обеих веток).
# Влить в мастера все коммит ы из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# cats.clear()
# for i in range(10):
#     cats.append(cats_to_move[i])
# for day in range(1, 366):
#     print('================== День {} =================='.format(day))
#     serge.act()
#     masha.act()
#     kolya.act()
#     for cat in cats:
#         cat.act()
#     print(serge)
#     print(masha)
#     print(kolya)
#     for cat in cats:
#         print(cat)
#     print(home)
# print('=========== Итоги союза {} и {} ==========='.format(serge.name, masha.name))
# print('Всего денег потрачено - {}, еды съедено - {}, шуб куплено - {}.'.format(
#     home.accounting, home.food_accounting, masha.fur_coats))

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
# Промоделировать - как часто могут случаться fails что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)


class Simulation:

    def experiment(self, salary, money_incidents, food_incidents):
        serge.salary = salary
        mon_fails_list = []
        food_fails_list = []
        ok = 1
        for _ in range(food_incidents):
            dice = randint(1, 366)
            food_fails_list.append(dice)
        for _ in range(money_incidents):
            dice = randint(1, 366)
            mon_fails_list.append(dice)
        for day in range(1, 366):
            if day in mon_fails_list:
                home.bedside_money /= 2
            if day in food_fails_list:
                home.food_in_the_fridge /= 2
            serge.act()
            masha.act()
            kolya.act()
            for cat in cats:
                cat.act()
                if not cat.cat_alive:
                    ok = 0
            if not serge.man_alive:
                ok = 0
            elif not masha.man_alive:
                ok = 0
            elif not kolya.man_alive:
                ok = 0
        if ok == 1:
            return len(cats)
        else:
            return '0'


def f1():
    print('*' * 54)


def f2():
    for _ in range(9000):
        life_to_life.append(Simulation())
        home_to_home.append(House(name='Хаусе'))
        serge_to_serge.append(Husband(name='Сережа'))
        masha_to_masha.append(Wife(name='Маша'))
        kolya_to_kolya.append(Child(name='Коля'))


# в итоге должен получится приблизительно такой код экспериментов
count = 0
n, N, k, K = 0, 2, 0, 2
cats, home_to_home, life_to_life, serge_to_serge, masha_to_masha, kolya_to_kolya = [], [], [], [], [], []

f2()
for food_incidents in range(n, N):
    for money_incidents in range(k, K):
        for salary in range(150, 401, 50):
            if salary == 150:
                f1()
                print('Инциденты с деньгами за год: ', money_incidents)
                print('Инциденты с едой за год: ', food_incidents)
            cats.clear()
            for i in range(16):
                count += 1
                cats.append(Cat(name='Test'))
                home, serge, masha, kolya = home_to_home[count], serge_to_serge[count], masha_to_masha[count],\
                    kolya_to_kolya[count]
                max_cats = life_to_life[count].experiment(
                    salary=salary, money_incidents=money_incidents, food_incidents=food_incidents)
                if max_cats == '0':
                    print(f'При зарплате {salary} максимально можно прокормить {i} котов')
                    break
                elif max_cats == 16:
                    print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
                cats.clear()
                del life_to_life[count]
                for _ in range(0, i + 1):
                    cats.append(Cat(name='Test'))

# В данной модели:
# Гарантированная случайная выживаемость - при максимальном пороге N - 1, K - 1.
# При значениях N и K выше имеет место появление смертности.
