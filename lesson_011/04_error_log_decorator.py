# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(arg):
    def inner_decorator(func):
        path = arg

        def surrogate(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except (ArithmeticError, ValueError) as exc:
                print(f'Hey, we got {type(exc)} here in {func.__name__}`s "{args}" or "{kwargs}": {exc}')
                with open(path, 'a', encoding='utf8') as file:
                    file.write(f'Hey, we got {type(exc)} here'
                               f' in {func.__name__}`s attribute(s) "{args}" or/and "{kwargs}": {exc}\n')

        return surrogate

    return inner_decorator


# Проверить работу на следующих функциях
# @log_errors
# def perky(param):
#     return param / 0
#
#
# perky(9j)
#
#
# @log_errors
# def check_line(line):
#     name, email, age = line.split(' ')
#     if not name.isalpha():
#         raise ValueError("it's not a name")
#     if '@' not in email or '.' not in email:
#         raise ValueError("it's not a email")
#     if not 10 <= int(age) <= 99:
#         raise ValueError('Age not in 10..99 range')
#
#
# lines = [
#     'Ярослав bxh@ya.ru 600',
#     'Земфира tslzp@mail.ru 52',
#     'Тролль nsocnzas.mail.ru 82',
#     'Джигурда wqxq@gmail.com 29',
#     'Земфира 86',
#     'Равшан wmsuuzsxi@mail.ru 35',
# ]
# for line in lines:
#     try:
#         check_line(line)
#     except Exception as exc:
#         print(f'Invalid format: {exc}')
# perky(param=42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
@log_errors('function_errors.log')
def func(param):
    return param / 0

func(6)
