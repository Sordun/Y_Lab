import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative")
            setattr(self, key, value)

    @abstractmethod
    def get_area(self) -> None:
        pass


class HeightShape(Shape):
    @abstractmethod
    def get_height(self) -> None:
        pass


class PrintResult:
    @staticmethod
    def round_result(value: float, decimal_places: int = 2) -> float:
        """
        :param value: The value to be rounded
        :param decimal_places: The precision after the decimal point the value should be rounded to
        :return: Number rounded to decimal_places precision
        """
        return round(value, decimal_places)


class Shape2D(Shape):
    """
    Flat figure.
    """

    @abstractmethod
    def get_perimeter(self) -> None:
        pass


class Circle(Shape2D):
    """A class for circle."""

    title = "Круг"

    def __init__(self, radius: float) -> None:
        """
        :param radius: Radius of the circle
        """
        super().__init__(radius=radius)

    def get_area(self) -> float:
        """Calculate circle area."""
        return math.pi * (self.radius**2)

    def get_perimeter(self) -> float:
        """Calculate circumference."""
        return 2 * math.pi * self.radius


class Rectangle(Shape2D):
    """A class for rectangle."""

    title = "Прямоугольник"

    def __init__(self, a, b) -> None:
        super().__init__(a=a, b=b)

    def get_perimeter(self) -> float:
        """Perimeter of a rectangle."""
        return (self.a + self.b) * 2

    def get_area(self) -> float:
        """The area of the rectangle."""
        return self.a * self.b


class Square(Rectangle):
    """A class for square."""

    title = "Квадрат"

    def __init__(self, a) -> None:
        super().__init__(a, a)


class Triangle(Shape2D, HeightShape):
    """A class for triangle."""

    title = "Треугольник"

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        :param a: Side x of the triangle
        :param b: Side y of the triangle
        :param c: Side z of the triangle
        """
        super().__init__(a=a, b=b, c=c)
        if self.c >= self.b + self.a:
            raise ValueError

    def get_area(self) -> float:
        """
        :return: Area of the triangle
        """
        half_perimeter = self.get_perimeter() / 2
        return math.sqrt(
            half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c)
        )

    def get_perimeter(self) -> float:
        """
        :return: Perimeter of the triangle
        """
        return self.a + self.b + self.c

    def get_height(self) -> tuple[float, float, float]:
        """
        :return: Height of the triangle
        """
        two_areas = 2 * self.get_area()
        return two_areas / self.a, two_areas / self.b, two_areas / self.c


class Rhombus(Shape2D, HeightShape):
    """A class for rhombus."""

    title = "Ромб"

    def __init__(self, d1: float, d2: float) -> None:
        super().__init__(d1=d1, d2=d2)

    def get_perimeter(self) -> float:
        """
        :return: Perimeter of the diamond
        """
        return 4 * math.sqrt((self.d1 / 2) ** 2 + (self.d2 / 2) ** 2)

    def get_area(self) -> float:
        """
        :return: Area of the diamond
        """
        return 0.5 * self.d1 * self.d2

    def get_height(self) -> float:
        """
        :return: Height of the diamond
        """
        return 2 * (self.d1 * self.d2) / self.get_perimeter()


class Trapezoid(Shape2D):
    """A class for trapezoid."""

    title = "Трапеция"

    def __init__(
        self,
        base: float,
        left_base_angle: float,
        right_base_angle: float,
        height: float,
    ) -> None:
        """
        :param base: Length of longer base side of the trapeze
        :param left_base_angle: Right base angle
        :param right_base_angle: Left base angle
        :param height: Height of the trapeze
        """
        super().__init__(base=base, left_base_angle=left_base_angle, right_base_angle=right_base_angle, height=height)
        self.right_side = self.get_right_leg()
        self.left_side = self.get_left_leg()
        self.upper_side = self.get_upper_base_side()
        if self.left_base_angle >= 90 or self.right_base_angle >= 90 or self.left_base_angle == self.right_base_angle:
            raise ValueError

    def get_right_leg(self) -> float:
        """
        :return: Right lateral side of the trapezoid
        """
        return self.height / math.sin(math.radians(self.right_base_angle))

    def get_left_leg(self) -> float:
        """
        :return: Left lateral side of the trapezoid
        """
        return self.height / math.sin(math.radians(self.left_base_angle))

    def get_upper_base_side(self) -> float:
        """
        :return: Shorter base of the trapezoid
        """
        return self.base - self.height * (
            1 / math.tan(math.radians(self.left_base_angle)) + 1 / math.tan(math.radians(self.right_base_angle))
        )

    def get_area(self) -> float:
        """
        :return: Area of the trapezoid
        """
        return (self.base + self.upper_side) / 2 * self.height

    def get_perimeter(self) -> float:
        """
        :return: Perimeter of the trapezoid
        """
        return self.base + self.right_side + self.left_side + self.upper_side


class Shape3D(Shape):
    """
    3-D shape prototype.
    """

    @abstractmethod
    def get_volume(self) -> None:
        pass


class Sphere(Shape3D):
    """A class for sphere"""

    title = "Сфера"

    def __init__(self, r: float) -> None:
        super().__init__(r=r)

    def get_area(self) -> float:
        """
        :return: Area of the sphere surface
        """
        return 4 * math.pi * self.r**2

    def get_volume(self) -> float:
        """
        :return: Volume of the sphere
        """
        return 4 / 3 * math.pi * self.r**3


class Parallelepiped(Shape3D):
    """A class for parallelepiped."""

    title = "Параллелепипед"

    def __init__(self, a: float, b: float, h: float) -> None:
        super().__init__(a=a, b=b, h=h)
        self.s = [Rectangle(a, b), Rectangle(b, h), Rectangle(a, h)]

    def get_area(self) -> float:
        """
        :return: Area of Rectangular Parallelepiped
        """
        sides_areas = [side.get_area() for side in self.s]
        return sum(sides_areas) * 2

    def get_volume(self) -> float:
        """
        :return: Volume of Rectangular Parallelepiped
        """
        return self.a * self.b * self.h


class Cube(Parallelepiped):
    """A class for cube."""

    title = "Куб"

    def __init__(self, a: float) -> None:
        super().__init__(a, a, a)

    @property
    def x(self):
        return self.a


class Pyramid(Shape3D):
    """A class for pyramid."""

    title = "Пирамида"

    def __init__(self, x: float, h: float) -> None:
        super().__init__(h=h)
        self.square = Square(x)

    @property
    def x(self):
        return self.square.a

    def get_area(self) -> float:
        """
        :return: Area of the pyramid
        """
        triangle_height = math.sqrt(self.h**2 + (1 / 4) * self.square.a**2)
        side_area = 2 * self.square.a * triangle_height
        return self.square.get_area() + side_area

    def get_volume(self) -> float:
        """
        :return: Volume of the pyramid
        """
        return (1 / 3) * self.square.get_area() * self.h


class Cylinder(Shape3D):
    """A class for cylinder"""

    title = "Цилиндр"

    def __init__(self, radius: float, h: float) -> None:
        """
        :param radius: Radius of the cylinder
        :param h: Height of the cylinder
        """
        super().__init__(h=h)
        self.circle = Circle(radius)

    def get_area(self) -> float:
        """
        :return: Area of the cylinder
        """
        return self.circle.get_perimeter() * self.h + 2 * self.circle.get_area()

    def get_volume(self) -> float:
        """
        :return: Volume of the cylinder
        """
        return self.circle.get_area() * self.h

    @property
    def radius(self):
        return self.circle.radius


class Cone(Cylinder):
    """A class for cone."""

    title = "Конус"

    def __init__(self, radius: float, h: float) -> None:
        super().__init__(radius, h)

    def get_area(self) -> float:
        """
        :return: Area of right circular cone
        """
        side_area = math.pi * self.circle.radius * self.get_cone_generator()
        return self.circle.get_area() + side_area

    def get_volume(self) -> float:
        """
        :return: Volume of right circular cone
        """
        return (1 / 3) * self.circle.get_area() * self.h

    def get_cone_generator(self) -> float:
        """
        :return: Generator line of right circular cone
        """
        return math.sqrt(self.circle.radius**2 + self.h**2)
