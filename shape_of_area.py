from abc import ABC, abstractmethod
import math


#  Абстрактный класс Shape
class Shape(ABC):  #  Наследование от ABC (для абстрактности)
    @abstractmethod
    def area(self):  #  Подклассы Shape должны переопределять метод area
        pass


#  Класс пряугольников
class Rectangle(Shape):  #  Наследование от Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):  #  Переопределение метода `area` для расчета площади
        return self.width * self.height


#  Класс кругов
class Circle(Shape):  #  Наследование от Shape
    def __init__(self, radius):
        self.radius = radius


    def area(self):  #  Переопределение метода `area` для расчета площади
        return math.pi * self.radius ** 2


#  Проверка
rect_1 = Rectangle(379721, 26010)
circle_1 = Circle(1)
print(f'Площадь прямоугольника: {rect_1.area()} квадратных единиц')
print(f'Площадь круга: {circle_1.area()} квадратных единиц')