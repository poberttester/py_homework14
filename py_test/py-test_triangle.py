from doc_test import triangle
import pytest


def test_py_triangle_is_equilateral():
    assert triangle.triangle_func(13, 13, 13) == 'Треугольник равносторонний'


def test_py_triangle_is_isosceles():
    assert triangle.triangle_func(17, 10, 17) == 'Треугольник равнобедренный'


def test_py_triangle_is_versatile():
    assert triangle.triangle_func(13, 15, 17) == 'Треугольник разносторонний'


def test_py_triangle_does_not_exist():
    assert triangle.triangle_func(10, 13, 23) == 'Треугольника с такими сторонами не существует'


if __name__ == "__main__":
    pytest.main(['-v'])
