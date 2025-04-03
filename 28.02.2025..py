"""
Задание 1:
Создайте абстрактный класс Транспорт
и два дочерних класса: Самолёт, Мотоцикл


Общие атрибуты: Топливо, Кол-во посадочных мест, Вид_руля, экипаж"
Методы: загрузка_транспорта(), Движение()
Атрибуты самолёта: Крылья, методы: Летать ()
Атрибыты мотоцикл: Отсутствие_крыши,
"""

import abc

class Transport(abc.ABC):
    def loading_transport(self):
        pass
    def movement(self):
        pass
class Airbus(Transport):
        def __init__(self, wings):
            self.wings = wings
            print(f"Airbus")
            print("I can fly")
        def loading_transport(self):
                print(f"Кол-во посадочных мест - 250")
        def movement(self):
                print(f"Способ передвижения - реактивный, в воздухе.")
class Motocycle(Transport):
        def __init__(self, no_roof ):
            self.no_roof = no_roof
            print(f"Motocycle")
            print(f"I don't roof")

        def loading_transport(self):
                print(f"Кол-во посадочных мест - 2")
        def movement(self):
                print(f"Способ передвижения - пневмоколёсный по грунту.")
obj1Moto = Motocycle("No roof")
# obj1Moto.roof()
obj1Moto.loading_transport()
obj1Moto.movement()

obj1Airbus = Airbus("Wings")
# obj1Airbus.fly()
obj1Airbus.loading_transport()
obj1Airbus.movement()






'''
Абстрактный класс - нельзя создать объект
Внутри храним общие методы и атрибуты
'''
import abc #для создания абстрактного класса
from abc import ABC

#если класс абстрактный, то __init__() не нужен
# class Shape(abc.ABC):
#     x=0
#     y=0
#     # @abc.abstractmethod
#     def area(self):
#         pass
#
#     # @abc.abstractmethod
#     def perimeter(self):
#         print("Посчитать периметр нельзя")
# class Square(Shape): # Square - дочерний   Shape  -родительский
#     side = 1 # значение по умолчанию, но мы можем передать своё
#     def __init__(self,side):
#         self.side = side
#     # переопределяем ф-цию
#     def area(self):
#         print(f" Площадь = {self.side*self.side}")
#
#     def perimeter(self):
#         print(f"Периметр квадрата = {self.side*4}")
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print(f"Площадь = {self.radius*3.14*self.radius}")
# objCircle = Circle(5)
# objCircle.perimeter()
# objCircle.area()
#
#
#
#
# side = int(input("Введите сторону фигуры:   "))
# objSquare = Square(side)
# #obj1Shape = Shape()
# objSquare.area()
# objSquare.perimeter()
