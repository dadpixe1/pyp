# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

from lesson_005.burger.my_burger import bread_func, pickle_func, mayonnaise_func, tomato_func, steak_func, cheese_func

print('Double with cheese recipe:')
bread_func(), pickle_func(), tomato_func(), mayonnaise_func(), cheese_func(), steak_func(), cheese_func(), steak_func(),
bread_func()
print('My burger recipe:')
bread_func(), tomato_func(), bread_func()