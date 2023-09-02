from doc_test import triangle
import unittest


class TestTriangle(unittest.TestCase):

    def test_triangle_is_equilateral(self):
        self.assertEqual(triangle.triangle_func(13, 13, 13), 'Треугольник равносторонний')

    def test_triangle_is_isosceles(self):
        self.assertEqual(triangle.triangle_func(17, 10, 17), 'Треугольник равнобедренный')

    def test_triangle_is_versatile(self):
        self.assertEqual(triangle.triangle_func(13, 15, 17), 'Треугольник разносторонний')

    def test_triangle_does_not_exist(self):
        self.assertEqual(triangle.triangle_func(10, 13, 23), 'Треугольника с такими сторонами не существует')


if __name__ == "__main__":
    unittest.main(verbosity=2)


