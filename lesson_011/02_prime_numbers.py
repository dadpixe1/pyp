# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#
#     def __init__(self, n):
#         self.n = n
#         self.prime_numbers = []
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         for number in range(2, self.n + 1):
#             if number == self.n:
#                 raise StopIteration()
#             for prime in self.prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 self.prime_numbers.append(number)
#                 return number
#
#
# prime_number_iterator = PrimeNumbers(n=1000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

# def lucky_numbers(n):
#     half = int(len(str(n)) / 2)
#     result_l = sum(int(x) for x in str(n)[:half] if len(str(n)) % 2 == 0)
#     result_r = sum(int(x) for x in str(n)[half:] if len(str(n)) % 2 == 0)
#     res_l, res_r = sum(int(x) for x in str(n)[:half + 1]), sum(int(x) for x in str(n)[half:])
#     if result_l > 0 and result_l == result_r or res_l == res_r:
#         return True
#
#
# print(lucky_numbers(92083))


# def palin_numbers(n):
#     half = int(len(str(n)) / 2)
#     result_l = (int(x) for x in str(n)[:half] if len(str(n)) % 2 == 0)
#     result_r = (int(x) for x in str(n)[half:] if len(str(n)) % 2 == 0)
#     res_l, res_r = (int(x) for x in str(n)[:half + 1]), (int(x) for x in str(n)[half:])
#     left_gen, right_gen = list(result_l), list(reversed(list(result_r)))
#     l_gen, r_gen = list(res_l), list(reversed(list(res_r)))
#     if left_gen is not None and left_gen == right_gen or l_gen == r_gen:
#         return True
#
#
# print(palin_numbers(723327))
