import unittest
from calculator import Circle, Rectangle, Square, Triangle, Rhombus, Trapezoid, PrintResult


class TestCircle(unittest.TestCase):
    radius = 5

    def setUp(self):
        self.test_circle = Circle(self.radius)

    def test_area_calculation(self):
        area = self.test_circle.get_area()
        self.assertEqual(PrintResult.round_result(area), 78.54)

    def test_perimeter_calculation(self):
        perimeter = self.test_circle.get_perimeter()
        self.assertEqual(PrintResult.round_result(perimeter), 31.42)


class TestRectangle(unittest.TestCase):
    x, y = 20, 30

    def setUp(self):
        self.test_rectangle = Rectangle(self.x, self.y)

    def test_area_calculation(self):
        area = self.test_rectangle.get_area()
        self.assertEqual(PrintResult.round_result(area), 600)

    def test_perimeter_calculation(self):
        perimeter = self.test_rectangle.get_perimeter()
        self.assertEqual(PrintResult.round_result(perimeter), 100)


class TestSquare(unittest.TestCase):
    x = 25

    def setUp(self):
        self.test_square = Square(self.x)

    def test_area_calculation(self):
        area = self.test_square.get_area()
        self.assertEqual(PrintResult.round_result(area), 625)

    def test_perimeter_calculation(self):
        perimeter = self.test_square.get_perimeter()
        self.assertEqual(PrintResult.round_result(perimeter), 100)


class TestRhombus(unittest.TestCase):
    d1, d2 = 20, 30

    def setUp(self):
        self.test_diamond = Rhombus(self.d1, self.d2)

    def test_area_calculation(self):
        area = self.test_diamond.get_area()
        self.assertEqual(PrintResult.round_result(area), 300)

    def test_perimeter_calculation(self):
        perimeter = self.test_diamond.get_perimeter()
        self.assertEqual(PrintResult.round_result(perimeter), 72.11)


class TestTrapezoid(unittest.TestCase):
    base = 8
    left_base_angle = 80
    right_base_angle = 55
    height = 5

    def setUp(self):
        self.test_trapeze = Trapezoid(self.base, self.left_base_angle, self.right_base_angle, self.height)

    def test_right_side_calculation(self):
        right_side = self.test_trapeze.get_right_leg()
        self.assertEqual(PrintResult.round_result(right_side), 6.1)

    def test_left_side_calculation(self):
        left_side = self.test_trapeze.get_left_leg()
        self.assertEqual(PrintResult.round_result(left_side), 5.08)

    def test_upper_side_calculation(self):
        upper_side = self.test_trapeze.get_upper_base_side()
        self.assertEqual(PrintResult.round_result(upper_side), 3.62)

    def test_area_calculation(self):
        area = self.test_trapeze.get_area()
        self.assertEqual(PrintResult.round_result(area), 29.04)

    def test_perimeter_calculation(self):
        perimeter = self.test_trapeze.get_perimeter()
        self.assertEqual(PrintResult.round_result(perimeter), 22.8)


class TestTriangle(unittest.TestCase):
    x, y, z = 3, 5, 5

    def setUp(self):
        self.test_triangle = Triangle(self.x, self.y, self.z)

    def test_area_calculation(self):
        area = self.test_triangle.get_area()
        self.assertEqual(PrintResult.round_result(area), 7.15)

    def test_perimeter_calculation(self):
        perimeter = self.test_triangle.get_perimeter()
        self.assertEqual(PrintResult.round_result(perimeter), 13)

    def test_height_calculation(self):
        heights = self.test_triangle.get_height()
        heights = [PrintResult.round_result(height) for height in heights]
        self.assertEqual(heights, [4.77, 2.86, 2.86])


if __name__ == "__main__":
    unittest.main()
