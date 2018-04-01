def section_3_1():
    """
    3.1. Rounding Numerical Values

    round(value, ndigits)
    """

    def test1():
        print(round(1.23, 1))
        print(round(1.27, 1))
        print(round(-1.27, 1))
        print(round(1627731, -1))
        print(round(1627731, -2))
        print(round(1627731, -3))

    def test2():
        x = 1.23456
        print(format(x, '0.2f'))
        print(format(x, '0.3f'))
        print('value is {:0.3f}'.format(x))


def section_3_2():
    """
    3.2. Performing Accurate Decimal Calculations
    避免浮点数运算结果的误差。
    decimal module
    """
    from decimal import Decimal

    def test1():
        a = Decimal('4.2')
        b = Decimal('2.1')
        print(a + b)


def section_3_3():
    """
    3.3. Formatting Numbers for Output
    format()
    """

    def test1():
        x = 1234.56789
        print(format(x, '0.2f'))
        print(format(x, '>10.1f'))
        print(format(x, '<10.1f'))
        print(format(x, '^10.1f'))
        print(format(x, ','))
        print(format(x, '0,.1f'))
        print(format(x, 'e'))
        print(format(x, 'E'))

    test1()


def section_3_4():
    """
    3.4. Working with Binary, Octal, and Hexadecimal Integers
    处理二进制、八进制、十六进制数
    """

    def test1():
        x = 1234
        print(bin(x))
        print(oct(x))
        print(hex(x))
        print(format(x, 'b'))
        print(format(x, 'o'))
        print(format(x, 'x'))

    def test2():
        print(int('4d2', 16))
        print(int('10011010010', 2))

    test2()


def section_3_5():
    """
    3.5. Packing and Unpacking Large Integers from Bytes
    整型数与字节串的转换
    int.from_bytes()
    """
    pass


def section_3_6():
    """
    3.6. Performing Complex-Valued Math
    实现复数运算

    complex(real, imag)
    """

    def test1():
        a = complex(2, 4)
        b = 3 - 5j
        print(a, b)
        print(a.real, a.imag, a.conjugate())

    test1()


def section_3_7():
    """
    3.7. Working with Infinity and NaNs
    """
    import math

    def test1():
        a = float('inf')
        b = float('-inf')
        c = float('nan')
        print(a, b, c)

    def test2():
        c = float('nan')
        d = float('nan')
        print(c == d)
        print(c is d)
        print(math.isnan(c))

    test2()


def section_3_8():
    """
    3.8. Calculating with Fractions
    fractions.Fraction
    """
    from fractions import Fraction

    def test1():
        a = Fraction(5, 4)
        b = Fraction(7, 16)
        print(a + b)
        print(a * b)
        c = a * b
        print(c.numerator, c.denominator)
        print(float(c))
        print(c.limit_denominator(8))
        x = 3.75
        print(Fraction(*x.as_integer_ratio()))

    test1()


def section_3_9():
    """
    3.9. Calculating with Large Numerical Arrays
    NumPy库
    """

    def test1():
        x = [1, 2, 3, 4]
        y = [5, 6, 7, 8]
        print(x * 2)
        # print(x + 10)
        print(x + y)

    def test2():
        # import numpy as np
        #
        # ax = np.array([1, 2, 3, 4])
        # ay = np.array([5, 6, 7, 8])
        pass

    test2()


def section_3_10():
    """
    3.10. Performing Matrix and Linear Algebra Calculations
    numpy
    // TO-DO
    """
    pass
