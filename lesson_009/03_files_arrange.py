# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в объектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - unzip проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk =
#   os.path.dirname =
#   os.path.join =
#   os.path.normpath
#   os.path.getmtime =
#   time.gmtime =
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов. :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class FilesSortedByData:

    def __init__(self, source_dir, dest_dir):
        self.current_dir = os.path.dirname(__file__)
        self.scan_dir = source_dir
        self.done_dir = dest_dir
        self.temp_dict = []
        self.temp_data = []
        self.scan()

    def scan(self):
        for dirpath, dirname, filename in os.walk(self.scan_dir):
            for file in filename:
                file_path = os.path.join(dirpath, file)
                dir_secs = os.path.getmtime(file_path)
                file_time = time.gmtime(dir_secs)
                line = file_time[0], file_time[1], file_path
                self.temp_data.append(line)
        self.folders_und_files()

    def folders_und_files(self):
        for year, month, path in sorted(self.temp_data):
            data = year, month
            if data in self.temp_dict:
                exist_folder_path = os.path.join(f'{self.current_dir}\\{self.done_dir}\\{year}\\{month}')
                shutil.copy2(src=path, dst=exist_folder_path)
            else:
                self.temp_dict.append(data)
                new_folder_path = f'{self.current_dir}\\{self.done_dir}\\{year}\\{month}'
                os.makedirs(new_folder_path)
                shutil.copy2(src=path, dst=new_folder_path)


FilesSortedByData(source_dir='D:\\m\\mvs\\pyp\\lesson_009\\icons', dest_dir='icons_by_year')
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
