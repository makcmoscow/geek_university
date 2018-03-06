# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
from Homework_1_5_easy import making_dir, listing_dir, deleting_dir

help = """
1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку
5. Quit
"""
while True:
    print(help)
    user_input = input()
    if not user_input:
        print('Выходим из программы')
        exit(0)
    else:
        try:
            user_input = int(user_input)
        except ValueError:
            print('Вы ввели не цифру')
    if user_input == 1:
        name_dir = str(input('Введите имя папки для перехода: '))
        try:
            os.chdir(name_dir)
            print('Успешно перешли в папку ', name_dir)
        except FileNotFoundError:
            print('Не существует папки с таким названием')

    if user_input == 2:
        listing_dir()
    if user_input == 3:
        name_dir = str(input('Введите имя удаляемой папки: '))
        try:
            deleting_dir(name_dir)
            print('Папка {} успешно удалена'.format(name_dir))
        except FileNotFoundError:
            print('Не существует папки с таким названием')
    if user_input == 4:
        try:
            name_dir = str(input('Введите имя создаваемой папки: '))
            making_dir(name_dir)
            print('Папка {} успешно создана'.format(name_dir))
        except:
            pass
    if user_input == 5:
        exit(0)
