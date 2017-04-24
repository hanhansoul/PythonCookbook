def section_4_1():
	"""
	4.1. Manually Consuming an Iterator
	不使用for循环，而使用next()来遍历迭代器
	StopIteration异常用于标识迭代终止，或标记None作为终止标识。
	next()
	"""

	def test1():
		with open('input.txt') as f:
			try:
				while True:
					line = next(f)
					print(line, end='')
			except StopIteration:
				pass

	def test2():
		with open('input.txt') as f:
			while True:
				line = next(f, None)
				if line is None:
					break
				print(line, end='')

def section_4_2():
	"""
	4.2. Delegating Iteration
	将一个包含list，tuple或其他可迭代对象的类作为一个自定义的迭代器。
	只需要实现类的__iter__()方法。
	"""

	class Node:
		def __init__(self, value):
			self._value = value
			self._children = []

		def __repr__(self):
			return 'Node({!r})'.format(self._value)

		def add_child(self, node):
			self._children.append(node)

		def __iter__(self):
			return iter(self._children)

	def test1():
		root = Node(0)
		child1 = Node(1)
		child2 = Node(2)
		root.add_child(child1)
		root.add_child(child2)
		for ch in root:
			print(ch)

def section_4_3():
	"""
	4.3. Creating New Iteration Patterns with Generators
	利用生成器创建新的迭代器模式。
	生成器只会在调用迭代器next()函数时才会继续运行，否则其会在yield位置阻塞直到下一次next()调用。
	"""

	def test1():
		def frange(start, stop, increment):
			x = start
			while x < stop:
				yield x
				x += increment

		for n in frange(0, 4, 0.5):
			print(n)

	def test2():
		def countdown(n):
			print('Starting counting from', n)
			while n > 0:
				yield n
				n -= 1
			print('finished!')

		c = countdown(3)
		print(next(c))
		print(next(c))
		print(next(c))
		print(next(c))

def section_4_4():
	"""
	4.4. Implementing the Iterator Protocol
	// TO-DO
	实现python的迭代器接口需要实现__iter__()函数返回一个迭代器对象，该迭代器对象实现了__next__()函数，并以一个StopIteration异常
	作为结束标识。
	这种实现迭代器的方式往往十分混乱，不利于阅读，因此推荐使用生成器的方式实现迭代功能。
	"""
	pass

def section_4_5():
	"""
	4.5. Iterating in Reverse
	对于长度无法确定，如文件，或没有实现__reversed__()方法的对象，需要将其转化为list再进行反向遍历，这种方式可能消耗大量的空间。
	可以通过重写__reversed__()生成器的方式实现反向遍历
	"""

	def test1():
		a = [1, 2, 3, 4]
		for x in reversed(a):
			print(x)

	def test2():
		class Countdown:
			def __init__(self, start):
				self.start = start

			def __iter__(self):
				n = self.start
				while n > 0:
					yield n
					n -= 1

			def __reversed__(self):
				n = 1
				while n < self.start:
					yield n
					n += 1

def section_4_6():
	"""
	4.6. Defining Generator Functions with Extra State
	自定义生成器，使返回值返回多个状态。
	利用tuple返回多个状态值。
	"""
	from collections import deque

	def test1():
		class linehistory:
			def __init__(self, lines, histlen=3):
				self.lines = lines
				self.history = deque(maxlen=histlen)

			def __iter__(self):
				for lineno, line in enumerate(self.lines, 1):
					self.history.append((lineno, line))
					yield line

			def clear(self):
				self.history.clear()

		with open('input.txt') as f:
			lines = linehistory(f)
			for line in lines:
				if 'python' in line:
					for lineno, hline in lines.history:
						print('{}:{}'.format(lineno, hline), end='')

def section_4_7():
	"""
	4.7. Taking a Slice of an Iterator
	itertools.islice()
	"""
	import itertools

	def test1():
		def count(n):
			while True:
				yield n
				n += 1

		c = count(0)
		for x in itertools.islice(c, 10, 20):
			print(x)

	test1()

def section_4_8():
	"""
	4.8. Skipping the First Part of an Iterable
	itertools.dropwhile
	"""
	pass

def section_4_9():
	"""
	4.9. Iterating Over All Possible Combinations or Permutations
	permutations()
	"""
	from itertools import permutations
	from itertools import combinations
	from itertools import combinations_with_replacement

	items = ['a', 'b', 'c']

	def test1():
		for p in permutations(items):
			print(p)

	def test2():
		for p in combinations(items, 3):
			print(p)
		print()
		for p in combinations(items, 2):
			print(p)
		print()
		for p in combinations(items, 1):
			print(p)
		print()
		for p in combinations_with_replacement(items, 3):
			print(p)

def section_4_10():
	"""
	4.10. Iterating Over the Index-Value Pairs of a Sequence
	在遍历序列时，同时返回元素所在的索引值。
	enumerate()将索引与元素值组成一个enumerator对象返回。
	"""
	my_list = ['a', 'b', 'c']

	def test1():
		for index, value in enumerate(my_list):
			print(index, value)

section_4_9()
