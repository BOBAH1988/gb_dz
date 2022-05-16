# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# my = (1, 'один', 1.0, True)
# for i in my:
#     print(type(i))

# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

# n = input('Введите через запятую список: ').split()
# for i in range(0, len(n), 2):
#     if i == len(n) -1:
#         break
#     n[i], n[i + 1] = n[i + 1], n[i]
# print(n)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

#n = int(input('Введите номер месяца: '))
# if 0 < n < 3 or n == 12:
#     print('Зима')
# elif 3 <= n <= 5:
#     print('Весна')
# elif 6 <= n <= 8:
#     print('Лето')
# elif 9 <= n <= 11:
#     print('Осень')
# else:
#     print('Такого месяца нет')

# n = int(input('Введите номер месяца: '))
# wi = [12, 1, 2]
# sp = [3, 4, 5]
# su = [6, 7, 8]
# ou = [9, 10, 11]
# for i in wi:
#     if n in wi:
#         print('Зима')
#         break
# for i in sp:
#     if n in sp:
#         print('Весна')
#         break
# for i in su:
#     if n in su:
#         print('Лето')
#         break
# for i in ou:
#     if n in ou:
#         print('Осень')
#         break

#n = int(input('Введите номер месяца: '))
# dic = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [5, 7, 8], 'Осень': [9, 10, 11]}
# for i in dic:
#     if n in dic[i]:
#         print(i)
#     else:
#         print('Такого месяца нет')
#         break

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
# первые 10 букв в слове.

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
# © geekbrains.ru
# 38название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика
# товара,
# например,
# название.
# Тогда
# значение
# —
# список
# значений-характеристик, например, список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }