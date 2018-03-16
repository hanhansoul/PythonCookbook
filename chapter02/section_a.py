def section_1_1():
    """
    2.1. Splitting Strings on Any of Multiple Delimiters
    根据多种不同分隔符来split一个字符串

    使用正则表达式
    re.split()
    """
    import re

    def test1():
        line = 'asdf fjkl; afed, fjke,asdf,      foo'
        print(re.split(r'[;,\s]\s*', line))

    def test2():
        line = 'asdf fjkl; afed, fjke,asdf,      foo'
        fields = re.split(r'(;|,|\s)\s*', line)
        print(fields)
        values = fields[::2]
        delimiters = fields[1::2] + ['']
        print(values)
        print(delimiters)


def section_2_2():
    """
    2.2. Matching Text at the Start or End of a String
    对字符串的首尾进行匹配，如文件扩展名或URL等。

    str.startswith()或str.endswith()
    """

    def test1():
        filename = 'spam.txt'
        print(filename.endswith('.txt'))
        print(filename.startswith('file:'))

        url = 'http://www.python.org'
        print(url.startswith('http:'))

    def test2():
        filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
        print([name for name in filenames if name.endswith(('.c', '.h'))])
        print(any(name.endswith('.py') for name in filenames))


def section_2_3():
    """
    2.3. Matching Strings Using Shell Wildcard Patterns

    fnmatch.fnmatch()和fnmatch.fnmatchcase()
    """
    from fnmatch import fnmatch, fnmatchcase

    def test1():
        print(fnmatch('foo.txt', '*.txt'))
        print(fnmatch('foo.txt', '?oo.txt'))
        print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
        names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
        print([name for name in names if fnmatch(name, 'Dat*.csv')])

    def test2():
        print(fnmatchcase('foo.txt', '*.txt'))
        print(fnmatchcase('foo.txt', '*.TXT'))


def section_2_4():
    """
    2.4. Matching and Searching for Text Patterns

    str.find()

    // TO-DO
    re.compile()
    match() / findall() / finditer()
    group()
    """

    def test1():
        text = 'yeah, but no, but yeah, but no, but yeah'
        print(text == 'yeah')  # 精确匹配
        print(text.find('no'))


def section_2_5():
    """
    2.5. Searching and Replacing Text
    str.replace()
    re.sub()
    """
    import re

    def test1():
        text = 'yeah, but no, but yeah, but no, but yeah'
        print(text.replace('yeah', 'yep'))
        print(text)

    def test2():
        text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
        print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
        print(text)


def section_2_6():
    """
    2.6. Searching and Replacing Case-Insensitive Text
    re.IGNORECASE
    """
    import re

    def test1():
        text = 'UPPER PYTHON, lower python, Mixed Python'
        print(re.findall('python', text, flags=re.IGNORECASE))
        print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

    test1()


def section_2_7():
    """
    2.7. Specifying a Regular Expression for the Shortest Match

    """


section_2_6()
