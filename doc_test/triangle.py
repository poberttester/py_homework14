
def triangle_func(a: int, b: int, c: int) -> str:
    """
    >>> triangle_func(3,3,3)
    'Треугольник равносторонний'

    >>> triangle_func(7,10,7)
    'Треугольник равнобедренный'

    >>> triangle_func(7,5,3)
    'Треугольник разносторонний'

    >>> triangle_func(7,4,3)
    'Треугольника с такими сторонами не существует'

    """
    message = "null"

    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            message = "Треугольник равносторонний"
            return message
        elif a == b or a == c or b == c:
            message = "Треугольник равнобедренный"
            return message
        else:
            message = "Треугольник разносторонний"
            return message
    else:
        message = "Треугольника с такими сторонами не существует"
        return message


if __name__ == '__main__':
    a = 2; b = 5; c = 3
    triangle_func(a, b, c)
    import doctest

    doctest.testmod(verbose=True)