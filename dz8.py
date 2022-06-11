# 1

# class Data:
#     def __init__(self, day_month_year):
#         # self.day = day
#         # self.month = month
#         # self.year = year
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         my_date = []
#
#         for i in day_month_year.split():
#             if i != '-': my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2019 >= year >= 0:
#                     return f'All right'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Data.extract(self.day_month_year)}'
#
# today = Data('11 - 1 - 2001')
# print(today)
# print(Data.valid(11, 11, 2022))
# print(today.valid(11, 13, 2011))
# print(Data.extract('11 - 11 - 2011'))
# print(today.extract('11 - 11 - 2020'))
# print(Data.valid(1, 11, 2000))

# 2

# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
# def div():
#     try:
#         user_num_1 = int(input('Введите делимое: '))
#         user_num_2 = int(input('Введите делитель: '))
#         if user_num_2 == 0:
#             raise OwnError("Делить на ноль нельзя!")
#         else:
#             res = user_num_1 / user_num_2
#             return res
#     except ValueError:
#         return "Вы ввели не число"
#     except OwnError as err:
#         return err
# print(div())

# 3

# class MyError(Exception):
#     def __init__(self):
#         pass
# class TypeCheck:
#     def __init__(self):
#         self.my_list = []
#     def check_value(self):
#         global user_val
#         while True:
#             try:
#                 try:
#                     user_val = int(input('Введите числа: '))
#                     ex = input(f'Всё отлично, добавляем "{user_val}" в список. Хотите продолжить? y/n: ').lower()
#                     self.my_list.append(user_val)
#                     if ex == 'n':
#                         print(self.my_list)
#                         break
#                 except ValueError:
#                     raise MyError
#             except MyError:
#                 ex = input(f"Вы ввели не число! Хотите продолжить? y/n: ").lower()
#                 if ex == 'n':
#                     print(self.my_list)
#                     break
#                 else:
#                     self.check_value()
# a = TypeCheck()
# a.check_value()

# 4

# class OfficeEquipment:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.items = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}
#     def income(self):
#         try:
#             name = input(f'Введите наименование: ')
#             price = int(input(f'Введите цену за ед: '))
#             quantity = int(input(f'Введите количество: '))
#             item = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
#             self.items.update(item)
#             print(self.items)
#         except ValueError:
#             print('Недопустимое значение!')
# class Printer(OfficeEquipment):
#     pass
# class Scanner(OfficeEquipment):
#     pass
# class Xerox(OfficeEquipment):
#     pass
# p = Printer('Hp', 2, 300)
# s = Scanner('Canon', 54000, 10)
# x = Xerox('Xerox', 7000, 15)
# p.income()
# s.income()
# x.income()

# 5
# class ComplexNumber:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __add__(self, other):
#         return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'
#     def __mul__(self, other):
#         return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'
# c_1 = ComplexNumber(4, -8)
# c_2 = ComplexNumber(6, 11)
# print(c_1 + c_2)
# print(c_1 * c_2)
