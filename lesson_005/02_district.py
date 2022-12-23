# -*- coding: utf-8 -*-
from pprint import pprint
# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from lesson_005.district import both_streets_folks

print('На районе живут')
for i in both_streets_folks():
    print(i)

# pprint(streets_list)
# from district.central_street.house1.room1 import folks as central_h1r1_folks
# from district.central_street.house1.room2 import folks as central_h1r2_folks
# from district.central_street.house2.room1 import folks as central_h2r1_folks
# from district.central_street.house2.room2 import folks as central_h2r2_folks
# from district.soviet_street.house1.room1 import folks as soviet_h1r1_folks
# from district.soviet_street.house1.room2 import folks as soviet_h1r2_folks
# from district.soviet_street.house2.room1 import folks as soviet_h2r1_folks
# from district.soviet_street.house2.room2 import folks as soviet_h2r2_folks
#
# inhabitants_list = [', '.join(central_h1r1_folks), '\n', ', '.join(central_h1r2_folks), '\n',
#                     ', '.join(central_h2r1_folks), '\n', ', '.join(central_h2r2_folks), '\n',
#                     ', '.join(soviet_h1r1_folks), '\n', ', '.join(soviet_h1r2_folks), '\n',
#                     ', '.join(soviet_h2r1_folks), '\n', ', '.join(soviet_h2r2_folks), '\n',]
#
# print('На районе живут', ', '.join(inhabitants_list))
# import os
#
# district = 'district'
# list1 = []
# list2 = []
#
# for street in os.listdir(district):
#     street_path = f"{district}/{street}"
#     list1.append('district')
#     list1.append(street)
#     for house in os.listdir(str(street_path)):
#         house_path = f"{district}/{street}/{house}"
#         list1.append(house)
#         for room in os.listdir(str(house_path)):
#             room_path = f"{district}/{street}/{house}/{room}"
#             list1.append(room)
# print(list1)
