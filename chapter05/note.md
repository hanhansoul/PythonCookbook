## chapter 5.1 (*)

文件的基本输入输出。

## chapter 5.2 (*)

print(file=output) print指定输出文件。

## chapter 5.3 (*)

文件输出时使用不同的行分隔符和行结束符。

print(content, sep=',', end='\n')

## chapter 5.4 (*)

输入输出二进制数据。

open("input", "rb") / open("input", "wb")

## chapter 5.5

仅当文件不存在时才创建并输出到该文件。

open("output", "xt")

## chapter 5.6

io.StringIO() / io.BytesIO()

对字符串或二进制数据进行模拟文件操作。

## chapter 5.7

读写压缩文件。

gzip / bz2

## chapter 5.8

按照固定长度迭代遍历文件。

iter(functools.partial(f.read, RECORD_SIZE), b'')

## chapter 5.9

readinto() 将二进制数据直接读入一个可变缓存中。