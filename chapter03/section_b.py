def sectoin_3_11():
	"""
	3.11. Picking Things at Random
	random
	"""
	import random

	values = [1, 2, 3, 4, 5, 6]

	def test1():
		print(random.choice(values))
		print(random.choice(values))
		print(random.choice(values))
		print(random.choice(values))

	def test2():
		print(random.sample(values, 2))
		print(random.sample(values, 2))
		print(random.sample(values, 3))
		print(random.sample(values, 3))

	def test3():
		print(random.shuffle(values))
		print(random.shuffle(values))

	def test4():
		print(random.randint(0, 10))
		print(random.random())

def section_3_12():
	"""
	3.12. Converting Days to Seconds, and Other Basic Time Conversions
	timedelta
	"""
	from datetime import timedelta
	from datetime import datetime

	def test1():
		a = timedelta(days=2, hours=6)
		b = timedelta(hours=4.5)
		c = a + b
		print(c)
		print(c.days)
		print(c.seconds)

	def test2():
		a = datetime(2012, 9, 23)
		print(a + timedelta(days=10))
		b = datetime(2012, 12, 21)
		d = b - a
		print(d.days)
		now = datetime.today()
		print(now)
		print(now + timedelta(minutes=10))

def section_3_13():
	"""
	3.13. Determining Last Friday’s Date
	"""
	pass

def section_3_14():
	"""
	3.14. Finding the Date Range for the Current Month
	// TO-DO
	"""
	pass

def section_3_15():
	"""
	3.15. Converting Strings into Datetimes
	"""
	from datetime import datetime

	def test1():
		text = '2012-09-20'
		y = datetime.strptime(text, '%Y-%m-%d')
		z = datetime.now()
		diff = z - y
		print(diff)

def section_3_16():
	"""
	3.16. Manipulating Dates Involving Time Zones
	"""
	pass


