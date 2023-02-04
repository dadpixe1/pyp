# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутствуют все три поля
# - поле имени содержит только буквы
# - поле email содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError =
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение) ff.isalpha() =
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение) =
# - поле возраст НЕ является числом от 10 до 99: ValueError =
# Вызов метода обернуть в try-except.

class NotNameError(Exception):

    def __init__(self, message='Поле имени содержит не только буквы.'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'NotNameError. {self.message}'


class NotEmailError(Exception):

    def __init__(self, message='Поле адреса почты не содержит @ или .'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'NotEmailError. {self.message}'


class Validation:

    def __init__(self, file_to_read):
        self.bad_log = 'registrations_bad.log'
        self.good_log = 'registrations_good.log'
        self.file_to_read = file_to_read
        self.log = []
        self.log_collect()

    def log_collect(self):
        with open(self.file_to_read, 'r', encoding='utf8') as file:
            for line in file:
                self.log.append(line)
        self.log_sort()

    def log_sort(self):
        line_count = 0
        for line in self.log:
            line_count += 1
            try:
                name, mail, age = line.split(' ')
                if not name.isalpha():
                    raise NotNameError
                elif '@' not in mail or '.' not in mail:
                    raise NotEmailError
                elif 10 > int(age) > 99:
                    raise ValueError
                else:
                    self.write_cleared_log(string=line_count, line=line)
            except (ValueError, NotNameError, NotEmailError) as exc:
                self.write_error(string=line_count, line=line, error=exc, error_type=type(exc))

    def write_error(self, string, line, error, error_type):
        with open(self.bad_log, 'a', encoding='utf8') as file:
            file.write(f'There is {error_type}: {error}. File: {self.file_to_read}. \nFile line {string}: {line}.')

    def write_cleared_log(self, string, line):
        with open(self.good_log, 'a', encoding='utf8') as file:
            file.write(f'From line {string} in file {self.file_to_read}, we have new user: {line}')


Validation('registrations.txt')
