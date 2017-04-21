def with_context_expression():
	"""
	with
	上下文管理器
	1.	上下文管理协议: __enter__() / __exit__()
	2.	上下文管理器: 支持上下文管理协议的对象，这种对象实现了__enter__() 和 __exit__() 方法。
		上下文管理器定义执行 with 语句时要建立的运行时上下文，负责执行 with 语句块上下文中的进入与退出操作。
		通常使用 with 语句调用上下文管理器，也可以通过直接调用其方法来使用。
	3.	运行时上下文: 由上下文管理器创建，通过上下文管理器的 __enter__() 和 __exit__() 方法实现，__enter__()
		方法在语句体执行之前进入运行时上下文，__exit__() 在语句体执行完后从运行时上下文退出。
		with 语句支持运行时上下文这一概念。
	4.	上下文表达式: with 语句中跟在关键字 with 之后的表达式，该表达式要返回一个上下文管理器对象。
	5.	语句体（with-body）：with 语句包裹起来的代码块，在执行语句体之前会调用上下文管理器的 __enter__() 方法，
		执行完语句体之后会执行 __exit__() 方法。
		python 对一些内建对象进行改进，加入了对上下文管理器的支持，可以用于 with 语句中，比如可以自动关闭文件、线程锁的自动获取和释放等。

		with context_expression [as target(s)]:
			with-body
	"""
	with open('input.txt', 'r') as fin:
		for l in fin:
			print(l)


def chapter_5_1():
	"""
	5.1. reading and writing text data
		you need to read or write text data, possibly in different text encodings such as ascii, utf-8, or utf-16.
	"""
	pass


def chapter_5_2():
	"""
	5.2. Printing to a File
	"""
	with open('output.txt', 'wt') as fout:
		print('redirect print to files', file=fout)


def chapter_5_3():
	"""
	5.3. Printing with a Different Separator or Line Ending
		You want to output data using print(), but you also want to change the separator character or line ending.
		print(content, sep='', end='')

		str.join() only works with strings
	"""
	print('abc', 'def', 'ghi', sep=', ', end='!!\n')


def chapter_5_4():
	"""
	5.4. Reading and Writing Binary Data
		You need to read or write binary data, such as that found in images, sound files, and so on.
		open() with 'rb' & 'wb'
	"""
	with open('binary_file.bin', 'wb') as fout:
		fout.write(b'BINARY IO')
	with open('binary_file.bin', 'rb') as fin:
		data = fin.read()
		print(data)

	'''
	difference between byte strings and text strings
	'''
	# Text string
	t = 'Hello World'
	print([x for x in t])
	b = b'Hello world'
	print([x for x in b])

	'''
		If you ever need to read or write text from a binary-mode file, make sure you remember
	to decode or encode it.
	'''
	with open('binary_file.bin', 'wb') as fout:
		text = 'Hello World'
		fout.write(text.encode('utf-8'))
	with open('binary_file.bin', 'rb') as fin:
		data = fin.read(16)
		text = data.decode('utf-8')
		print(text, data, sep='\n')
	'''
		objects such as arrays and C structures can be used for writing without any kind of intermediate
	conversion to a bytes object.
	'''
	import array
	nums = array.array('i', [1, 2, 3, 4])
	with open('binary_file.bin', 'wb') as fout:
		fout.write(nums)
	out = array.array('i', [0] * 10)
	with open('binary_file.bin', 'rb') as fin:
		fin.readinto(out)
		print(out)


def chapter_5_5():
	"""
	5.5. Writing to a File That Doesn’t Already Exist
		'x' mode in open()
		Python 3 specific extension to the open() function.
	"""
	with open('new_output.txt', 'xt') as fout:
		fout.write('test')
	with open('new_output.txt', 'rt') as fin:
		data = fin.read()
		print(data)


def chapter_5_6():
	"""
	5.6. Performing I/O Operations on a String
		io.StringIO() / io.ByteIO()
		You want to feed a text or binary string to code that’s been written to operate on file-like objects instead.
		In unit tests, you might use StringIO to create a file-like object containing test data that’s fed into a
	function that would otherwise work with a normal file.
		Be aware that StringIO and BytesIO instances don’t have a proper integer file descriptor. Thus, they do not work
	with code that requires the use of a real system-level file such as a file, pipe, or socket.
	"""
	import io
	s = io.StringIO()
	s.write('Hello World\n')
	print(s)
	print('This is a test', file=s)
	# Get all of the data written so far
	print(s.getvalue())
	# Wrap a file interface around an existing string
	s = io.StringIO('Hello_World\n')
	print(s.read(4))
	print(s.read())


def chapter_5_7():
	"""
	5.7. Reading and Writing Compressed Datafiles
		gzip.open() / bz2.open()
		You need to read or write data in a file with gzip or bz2 compression.
	"""
	pass


def chapter_5_8():
	"""
	5.8. Iterating Over Fixed-Sized Records
		iter() / functools.partial()
		Instead of iterating over a file by lines, you want to iterate over a collection of fixed sized
	records or chunks.
		iter() can create an iterator if you pass it a callable and a sentinel value.
	"""
	from functools import partial
	RECORD_SIZE = 32
	with open('input.data', 'rb') as f:
		records = iter(partial(f.read, RECORD_SIZE), b'')
		for r in records:
			print(r)


def chapter_5_9():
	"""
	???
	5.9. Reading Binary Data into a Mutable Buffer
	readinto()
	read binary data directly into a mutable buffer without any intermediate copying.
	"""
	import os.path

	def read_into_buffer(filename):
		buf = bytearray(os.path.getsize(filename))
		with open(filename, 'rb') as fin:
			fin.readinto(buf)
		return buf

	with open('sample.bin', 'wb') as fout:
		fout.write(b'Hello World')
	buf = read_into_buffer('sample.bin')
	print(buf)
