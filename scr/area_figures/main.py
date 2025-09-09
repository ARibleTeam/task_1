from abc import ABC
from math import pi, sqrt

class Figure(ABC):
    """Базовый абстрактный класс геометрической фигуры.

    Определяет интерфейс для доступа к площади фигуры через свойство
    `area` (геттер и сеттер). Конкретные фигуры должны переопределять
    соответствующие методы.
    """
    def __init__(self):
        """Инициализирует базовую фигуру.

        В базовом классе дополнительных параметров нет.
        """
        pass
    
    @property
    def area(self):
        """Возвращает площадь фигуры.

        Должно быть реализовано в подклассах.
        """
        pass
    
    @area.setter
    def area(self):
        """Устанавливает площадь фигуры.

        Сеттер должен быть реализован в подклассах и изменять
        определяющие параметры фигуры так, чтобы соответствовать
        новой площади.
        """
        pass

class Circle(Figure):
    """Окружность с заданным радиусом."""
    def __init__(self, radius):
        """Создаёт окружность.

        Args:
            radius (int | float): Радиус окружности (положительное число).

        Raises:
            ValueError: Если радиус не число или не положительный.
        """
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Радиус должен быть положительным числом!")
        self.radius = radius

    @property
    def area(self):
        """Площадь окружности.

        Returns:
            float: Площадь, вычисленная как `pi * radius ** 2`.
        """
        return pi*self.radius**2
    
    @area.setter
    def area(self, area):
        """Задаёт площадь окружности и пересчитывает радиус.

        Args:
            area (int | float): Новая площадь (положительное число).

        Raises:
            ValueError: Если площадь неположительная или неверного типа.
        """
        if area <= 0:
            raise ValueError("Ты бы еще строкой площадь передал!") # немного юмора
        elif not isinstance(area, (int, float)):
           raise ValueError("Хуже некуда!") # немного юмора 
        
        self.radius = sqrt(area/pi)

class Triangle(Figure):
    """Треугольник по трём сторонам."""
    def __init__(self, a, b, c):
        """Создаёт треугольник по длинам сторон.

        Args:
            a (int | float): Длина стороны a (положительное число).
            b (int | float): Длина стороны b (положительное число).
            c (int | float): Длина стороны c (положительное число).

        Raises:
            ValueError: Если какая-либо из сторон не число или не положительна.
        """
        if not all(isinstance(side, (int, float)) and side > 0 for side in (a, b, c)):
            raise ValueError("Все стороны должны быть положительными числами!")
        self.a = a
        self.b = b
        self.c = c
        self.is_rectangular = self.__is_rectangular()
    
    def __is_rectangular(self):
        a2 = self.a**2
        b2 = self.b**2
        c2 = self.c**2
        return (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)
        
    @property
    def area(self):
        """Площадь треугольника по формуле Герона.

        Returns:
            float: Площадь треугольника.
        """

        p = (self.a + self.b + self.c) / 2 # формула Герона с полупериметром
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    
    @area.setter
    def area(self):
        """Сеттер площади треугольника (не реализовал)."""
        pass