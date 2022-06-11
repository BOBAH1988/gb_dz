# 1. Создать класс TrafficLight (светофор). Определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
class svet:
    color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i != 3:
            print(svet.color[i])
            if i == 0:
                sleep(5)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1
n = svet()
n.running()

# 2. Реализовать класс Road (дорога). Определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса; атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна; проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#         self.weight = 25
#         self.height = 5
#     def mass(self):
#         mass = self._length * self._width * self.weight * self.height / 1000
#         print(f'Для покрытия дороги неободимо {round(mass)} т')
# r = Road(5000, 20)
# r.mass()

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}; создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income); проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": int(wage), "bonus": int(bonus)}
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#     def get_total_income(self):
#         return self._income["wage"] + self._income["bonus"]
# n = Position('Vasya', 'Pupkin', 'manager', '75000', '5000')
# print(n.get_full_name(), n.get_total_income())

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

# class Car:
#     def __init__(self, name, speed, color, is_police=False):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
#     def go(self):
#         return f'{self.name} поехала.'
#     def stop(self):
#         return f'\n {self.name} остановилась.'
#     def turn(self, direction):
#         return f'\n {self.name} повернула {direction}'
#     def show_speed(self):
#         return f'\nВаша скорость: {self.speed}'
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             return f'\nВаша скорость выше допустимой: {self.speed}'
#         else:
#             return f'Ваша скорость в норме:'
# class SportCar(Car):
#     pass
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             return f'\nВаша скорость выше допустимой: {self.speed}'
#         else:
#             return f'Скорость {self.name} в норме'
# class PoliceCar(Car):
#     pass
# town = TownCar('БМВ', 60, 'синяя', False)
# print(town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())
#
# sport = SportCar('Ауди ТТ', 170, 'черный', False)
# print(sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())
#
# work = WorkCar('Ниссан', 90, 'красный', False)
# print(work.go(), work.show_speed(), work.turn('направо'), work.stop())
#
# police = PoliceCar('Вольво', 100, 'белый', True)
# print(police.go(), police.show_speed(), police.turn('направо'), police.stop())

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# class Stationery:
#     def __init__(self, title):
#         self.title = title
#     def draw(self):
#         return f'Запуск отрисовки'
# class Pen(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
# class Pencil(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
# class Handle(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
# pen = Pen('ручкой')
# print(pen.draw())
# pencil = Pencil('карандашем')
# print(pencil.draw())
# handle = Handle('маркером')
# print(handle.draw())
