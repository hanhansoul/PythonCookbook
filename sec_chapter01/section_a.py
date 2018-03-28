def chapter_1_4():
    """
    字符串左对齐，居中对齐，右对齐
    ljust
    rjust
    center
    """

    def test1():
        print('hej'.ljust(20))
        print('hej'.center(20))
        print('hej'.rjust(20))


def chapter_1_5():
    """
    去除字符串两端空格
    lstrip
    strip
    rstrip

    strip(string)
    去除指定的字符。
    """

    def test1():
        s = '   abdc   '
        print(s.lstrip())
        print(s.strip())
        print(s.rstrip())

    def test2():
        x = 'xyxxyy  hejyz  yyx'
        print(x.strip('xy'))


def chpater_1_5():
    """
    合并字符串
    join
    """
    pass


def chapter_1_7():
    """
    反转字符串
    """

    def test1():
        s = 'abcdefghijklmn'
        reversedString = s[::-1]
