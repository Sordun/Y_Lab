import abc
import functools
from math import pi, sqrt, tan


def rounding_decorator(decimal_places: int):
    """
    Decorator for rounding the result
    Arguments:
        decimal_places - how many characters to round
    """

    def decorator_wrapper(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return round(result, decimal_places)

        return wrapper

    return decorator_wrapper


class Shape:
    """
    An abstract class for geometric figures.
    """

    @classmethod
    def get_print_data(cls) -> dict:
        parent_data = {}
        if not cls is Shape:
            parent_data = cls.__bases__[0].get_print_data()

        if hasattr(cls, 'print_data'):
            result = {}
            result.update(cls.print_data)
            result.update(parent_data)
            return result

        return parent_data


class Shape2D(Shape):
    """
    Flat figure.
    """
    print_data = {
        'perimeter': 'Периметр',
        'area': 'Площадь',
    }

    @abc.abstractmethod
    def perimeter(self) -> float:
        """Shape perimeter."""
        pass

    @abc.abstractmethod
    def area(self) -> float:
        """Figure area."""
        pass


class Circle(Shape2D):
    """A class for circle."""

    title = 'Круг'
    params = {
        'r': 'Радиус',
    }

    print_data = {
        'diam': 'Диаметр',
        'area': 'Площадь',
        'perimeter': 'Периметр',
    }

    def __init__(self, r) -> None:
        super().__init__()
        self.__r = r

    @rounding_decorator(2)
    def diam(self) -> float:
        """Circle diameter."""
        return self.__r * 2

    @rounding_decorator(2)
    def area(self) -> float:
        """Calculate circle area."""
        return pi * self.__r * self.__r

    @rounding_decorator(2)
    def perimeter(self) -> float:
        """Calculate circumference."""
        return 2 * pi * self.__r


class Rectangle(Shape2D):
    """A class for rectangle."""

    title = 'Прямоугольник'
    params = {
        'a': 'сторона A',
        'b': 'сторона B',
    }
    print_data = {
        'diagonal': 'Диагональ',
    }

    def __init__(self, a, b) -> None:
        super().__init__()
        self.__a, self.__b = a, b

    @rounding_decorator(2)
    def perimeter(self) -> float:
        """Perimeter of a rectangle."""
        return (self.__a + self.__b) * 2

    @rounding_decorator(2)
    def area(self) -> float:
        """The area of the rectangle."""
        return self.__a * self.__b

    @rounding_decorator(2)
    def diagonal(self) -> float:
        """Diagonal of the rectangle."""
        return sqrt(pow(self.__a, 2) + pow(self.__b, 2))


class Square(Rectangle):
    """A class for square."""

    title = 'Квадрат'
    params = {
        'a': 'сторона A',
    }

    def __init__(self, a) -> None:
        super().__init__(a, a)


class Triangle(Shape2D):
    """A class for triangle."""

    title = 'Треугольник'
    params = {
        'a': 'сторона A',
        'b': 'сторона B',
        'c': 'сторона C',
    }
    print_data = {
        'radius': 'Радиус вписанной окружности',
    }

    def __init__(self, a, b, c) -> None:
        super().__init__()
        self.__a = a
        self.__b = b
        self.__c = c

    @rounding_decorator(2)
    def perimeter(self) -> float:
        """Perimeter of a triangle."""
        return self.__a + self.__b + self.__c

    @rounding_decorator(2)
    def area(self) -> float:
        """Area of a triangle."""
        p = self.perimeter() / 2
        return sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    @rounding_decorator(2)
    def radius(self) -> float:
        """The radius of the inscribed circle."""
        p = self.perimeter()
        return sqrt(((p - self.__a) * (p - self.__b) * (p - self.__c)) / p)


class Rhombus(Shape2D):
    """A class for rhombus."""

    title = 'Ромб'
    params = {
        'd1': 'Диагональ 1',
        'd2': 'Диагональ 2',
    }

    def __init__(self, d1, d2) -> None:
        super().__init__()
        self.__d1 = d1
        self.__d2 = d2

    @rounding_decorator(2)
    def perimeter(self) -> float:
        """The perimeter of the rhombus."""
        return sqrt(self.__d1 ** 2 + self.__d2 ** 2) * 2

    @rounding_decorator(2)
    def area(self) -> float:
        """The area of the rhombus."""
        return (self.__d1 * self.__d2) / 2


class Trapezoid(Shape2D):
    """A class for trapezoid."""

    title = 'Трапеция'
    params = {
        'a': 'Сторона A (нижняя)',
        'b': 'Сторона B (верхняя)',
        'c': 'Сторона C',
        'd': 'Сторона D',
        'h': 'Высота H',
    }
    print_data = {
        'diagonals': 'Диагонали',
    }

    def __init__(self, a, b, c, d, h) -> None:
        super().__init__()
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__h = h

    @rounding_decorator(2)
    def perimeter(self) -> float:
        """Calculate trapezoid perimeter."""
        return self.__a + self.__b + self.__c + self.__d

    @rounding_decorator(2)
    def area(self) -> float:
        """Calculate trapezoid area."""
        return (self.__a + self.__b) / 2 * self.__h

    @rounding_decorator(2)
    def get_d1(self) -> float:
        """First diagonal."""
        try:
            return sqrt(pow(self.__d, 2) + self.__a * self.__b - self.__a * (pow(self.__d, 2) - pow(self.__c, 2)) /
                        (self.__a - self.__b))
        except ValueError:
            return 0

    @rounding_decorator(2)
    def get_d2(self) -> float:
        """Second diagonal."""
        try:
            return sqrt(pow(self.__c, 2) + self.__a * self.__b - self.__a * (pow(self.__c, 2) - pow(self.__d, 2)) /
                        (self.__a - self.__b))
        except ValueError:
            return 0

    def diagonals(self) -> tuple:
        """The diagonals of the trapezoid."""
        return self.get_d1(), self.get_d2()


class Shape3D(Shape):
    """
    3-D shape prototype.
    """

    print_data = {
        'surface_area': 'Площадь поверхности',
        'volume': 'Объем',
    }

    @abc.abstractmethod
    def surface_area(self) -> float:
        """The surface area of the figure."""
        pass

    @abc.abstractmethod
    def volume(self) -> float:
        """The volume of the figure."""
        pass


class Sphere(Shape3D):
    """A class for sphere"""

    title = 'Сфера'
    params = {
        'r': 'Радиус',
    }
    print_data = {
        'diam': 'Диаметр',
    }

    def __init__(self, r) -> None:
        super().__init__()
        self.__r = r

    @rounding_decorator(2)
    def surface_area(self) -> float:
        """Surface area of a sphere."""
        return 4 * pi * self.__r ** 2

    @rounding_decorator(2)
    def volume(self) -> float:
        """The volume of the sphere."""
        return 4 * pi * self.__r ** 3 / 3

    @rounding_decorator(2)
    def diam(self) -> float:
        """The diameter of the sphere."""
        return self.__r * 2


class Parallelepiped(Shape3D):
    """A class for parallelepiped."""

    title = 'Параллелепипед'
    params = {
        'a': 'Сторона A',
        'b': 'Сторона B',
        'h': 'Высота'
    }
    print_data = {
        'diagonal': 'Диагональ',
    }

    def __init__(self, a, b, h) -> None:
        super().__init__()
        self.__a = a
        self.__b = b
        self.__h = h

    @rounding_decorator(2)
    def surface_area(self) -> float:
        """Surface area of a parallelepiped."""
        return 2 * (self.__a * self.__b + self.__a * self.__h + self.__b * self.__h)

    @rounding_decorator(2)
    def volume(self) -> float:
        """The volume of the parallelepiped."""
        return self.__a * self.__b * self.__h

    @rounding_decorator(2)
    def diagonal(self) -> float:
        """Diagonal of a parallelepiped."""
        return sqrt(pow(self.__a, 2) + pow(self.__b, 2) + pow(self.__h, 2))


class Cube(Parallelepiped):
    """A class for cube."""

    title = 'Куб'
    params = {
        'a': 'Сторона A',
    }

    def __init__(self, a) -> None:
        super().__init__(a, a, a)


class Pyramid(Shape3D):
    """A class for pyramid."""

    title = 'Пирамида'
    params = {
        'a': 'Сторона',
        'h': 'Высота',
        'n': 'Количество сторон',
    }

    def __init__(self, a, h, n) -> None:
        super().__init__()
        self.__a = a
        self.__h = h
        self.__n = n

    @rounding_decorator(2)
    def surface_area(self) -> float:
        """The surface area of the pyramid."""
        segment = self.__a / (2 * tan(180 / self.__n))
        return (self.__n * self.__a) * (segment + sqrt(pow(self.__h, 2) + pow(segment, 2))) / 2

    @rounding_decorator(2)
    def volume(self) -> float:
        """The volume of the pyramid."""
        return (self.__n * self.__a ** 2 * self.__h) / (12 * tan(180 / self.__n))


class Cylinder(Shape3D):
    """A class for cylinder"""

    title = 'Цилиндр'
    params = {
        'r': 'Радиус',
        'h': 'Высота',
    }

    def __init__(self, r, h) -> None:
        super().__init__()
        self.__r, self.__h = r, h

    @rounding_decorator(2)
    def surface_area(self) -> float:
        """Cylinder surface area."""
        return 2 * pi * self.__r * (self.__r + self.__h)

    @rounding_decorator(2)
    def volume(self) -> float:
        """Cylinder volume."""
        return pi * self.__r ** 2 * self.__h


class Cone(Shape3D):
    """A class for cone."""

    title = 'Конус'
    params = {
        'r': 'Радиус',
        'h': 'Длина стороны',
    }

    def __init__(self, r, h) -> None:
        super().__init__()
        self.__r, self.__h = r, h

    @rounding_decorator(2)
    def surface_height(self) -> float:
        """Cone height."""
        return sqrt(pow(self.__h, 2) - pow(self.__r, 2))

    @rounding_decorator(2)
    def surface_area(self) -> float:
        """Cone surface area."""
        return pi * self.__r * (self.__r + self.__h)

    @rounding_decorator(2)
    def volume(self) -> float:
        """The volume of the cone."""
        v = self.surface_height()
        return pi * self.__r ** 2 * v / 3


SHAPES = {
    1: Circle,
    2: Rectangle,
    3: Square,
    4: Triangle,
    5: Rhombus,
    6: Trapezoid,
    7: Sphere,
    8: Cube,
    9: Parallelepiped,
    10: Pyramid,
    11: Cylinder,
    12: Cone,
}


def run() -> None:
    """Starting calculations."""
    print('Варианты фигур\n')
    shapes_list_text = ''

    for num, shape_class in SHAPES.items():
        shapes_list_text += f'{num} - {shape_class.title}\n'
    print(shapes_list_text)

    correct_input = False
    while not correct_input:
        try:
            shape_num = int(input("Введите номер фигуры: "))
            if shape_num not in SHAPES:
                print('Неправильный номер фигуры')
                print('Принимаются только цифры указанные выше')
            else:
                correct_input = True
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Принимаются только цифры указанные выше')

    shape_class = SHAPES[shape_num]
    params_list_text = 'Вводите параметры через пробел:\n'

    for name, description in shape_class.params.items():
        params_list_text += f'{name} - {description}\n'

    params_text = input(params_list_text)
    params = [float(i) for i in params_text.split()]
    shape_instance = shape_class(*params)

    for method_name, method_description in shape_instance.get_print_data().items():
        print(f'{method_description}: {getattr(shape_instance, method_name)()}')


def main() -> None:
    end_response = None

    while True:
        run()

        correct_input = False
        while not correct_input:
            end_response = input('Хотите продолжить вычисления (или выйти)? Y / N \n')

            if end_response.upper() not in {'Y', 'N'}:
                print('Некорректный ввод')
            else:
                correct_input = True

        if end_response.upper() == 'N':
            break


if __name__ == '__main__':
    main()
