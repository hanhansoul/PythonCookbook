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
	
	"""

section_3_4()
