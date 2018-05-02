def section_2_10():
    """
    2.10. Working with Unicode Characters in Regular Expressions
    """
    pass


def section_2_11():
    """
    2.11. Stripping Unwanted Characters from Strings
    删除字符串中首尾不需要的字符，如多余的空格

    strip() / lstrip() / rstrip()
    """

    def test1():
        s = '    hello world  \n'
        print(s.strip())
        print(s.lstrip())
        print(s.rstrip())
        t = '-----hello====='
        print(t.lstrip('-'))
        print(t.rstrip('-='))


def section_2_12():
    """
    2.12. Sanitizing and Cleaning Up Text
    """
    pass


def section_2_13():
    """
    2.13. Aligning Text Strings
    ljust() / rjust() / center()
    format()
    """

    def test1():
        text = 'Hello World'
        print(text.ljust(20))
        print(text.rjust(20))
        print(text.center(20))
        print(text)
        print(text.ljust(20, '='))
        print(text.rjust(20, '*'))

    def test2():
        text = 'Hello World'
        print(format(text, '>20'))
        print(format(text, '<20'))
        print(format(text, '^20'))
        print('{:>10s} {:>10s}'.format('Hello', 'World'))


def section_2_14():
    """
    2.14. Combining and Concatenating Strings
    join()
    """

    def test1():
        parts = ['Is', 'Chicago', 'Not', 'Chicago?']
        print(' '.join(parts))
        print(','.join(parts))
        print(''.join(parts))


def section_2_15():
    """
    2.15. Interpolating Variables in Strings
    对一个字符串模板中的某些占位符进行替换
    format() / format_map()
    """

    def test1():
        s = '{name} has {n} messages.'
        print(s.format(name='Guido', n=37))

    def test2():
        s = '{name} has {n} messages.'
        name = 'Guido'
        n = 37
        print(s.format_map(vars()))
        print(vars())

    test2()


def section_2_16():
    """
    2.16. Reformatting Text to a Fixed Number of Columns
    将长string重新格式化成用户指定的行数
    textwrap
    """
    import textwrap

    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
		the eyes, not around the eyes, don't look around the eyes, \
		look into my eyes, you're under."

    def test1():
        print(textwrap.fill(s, 70))
        print(textwrap.fill(s, 40))
        print(textwrap.fill(s, 40, initial_indent='    '))
        print(textwrap.fill(s, 40, subsequent_indent='    '))


def section_2_17():
    """
    2.17. Handling HTML and XML Entities in Text
    将html或xml文件中的&entity;等特殊字符转换为对应的文本
    html module
    """
    import html

    def test1():
        s = 'Elements are written as "<tag>text</tag>".'
        print(s)
        print(html.escape(s))
        print(html.escape(s, quote=False))


def section_2_18():
    """
    2.18. Tokenizing Text
    将一个字符换从左往右转义成一个token流
    """
    pass


def section_2_19():
    pass


def section_2_20():
    """
    2.20. Performing Text Operations on Byte Strings
    """
    pass
