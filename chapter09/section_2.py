exec_chpt = 0


def chapter_9_13():
	"""
	9.13. Using a Metaclass to Control Instance Creation
		You want to change the way in which instances are created in order to implement singletons,
	caching, or other similar features.
	"""

	class NoInstance(type):
		def __call__(self, *args, **kwargs):
			raise TypeError("Can't instantiate directly")

	class Spam(metaclass=NoInstance):
		@staticmethod
		def grok(x):
			print('Spam.grok')

	Spam.grok(10)

	# Spam()

	# Singleton
	class Singleton(type):
		def __init__(self, *args, **kwargs):
			self.__instance = None
			super().__init__(*args, **kwargs)

		def __call__(self, *args, **kwargs):
			if self.__instance is None:
				self.__instance = super(Singleton, self).__call__(*args, **kwargs)
				return self.__instance
			else:
				return self.__instance

	class Spam_single(metaclass=Singleton):
		def __init__(self):
			print('Creating Spam')

	a = Spam_single()
	b = Spam_single()
	c = Spam_single()
	print(a is b)
	print(b is c)

	import weakref
	class Cached(type):
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.__cache = weakref.WeakValueDictionary()

		def __call__(self, *args, **kwargs):
			if args in self.__cache:
				return self.__cache[args]
			else:
				obj = super().__call__(*args)
				self.__cache[args] = obj
				return obj

	class Spam_cached(metaclass=Cached):
		def __init__(self, name):
			print('Creating Spam({!r})'.format(name))
			self.name = name

	a = Spam_cached('Guido')
	b = Spam_cached('Diana')
	c = Spam_cached('Guido')
	print(a is b)
	print(a is c)


def chapter_9_14():
	"""
	9.14. Capturing Class Attribute Definition Order
		metaclass
		You want to automatically record the order in which attributes and methods are defined
	inside a class body so that you can use it in various operations (e.g., serializing, mapping
	to databases, etc.).
	"""
	from collections import OrderedDict
	class Typed:
		_expected_type = type(None)

		def __init__(self, name=None):
			self.name = name

		def __set__(self, instance, value):
			if not isinstance(value, self._expected_type):
				raise TypeError('Expected ' + str(self._expected_type))
			instance.__dict__[self._name] = value

	class Integer(Typed):
		_expected_type = int

	class Float(Typed):
		_expected_type = float

	class String(Typed):
		_expected_type = str

	class orderedMeta(type):
		def __new__(cls, clsname, bases, clsdict):
			d = dict(clsdict)
			order = []
			for name, value in clsdict.items():
				if isinstance(value, Typed):
					value._name = name
					order.append(name)
			d['_order'] = order
			return type.__new__(cls, clsname, bases, d)

		@classmethod
		def __prepare__(cls, clsname, bases):
			return OrderedDict()


exec_chpt = chapter_9_14

exec_chpt()
