def chapter_5_11():
    """
    文件名和路径名操作。
    """
    import os

    def test1():
        path = "/users/beazley/data/data.csv"
        print(os.path.basename(path))
        print(os.path.dirname(path))
        print(os.path.join('tmp', 'data', os.path.basename(path)))
        print(os.path.splitext(path))


def chapter_5_12():
    """
    获取文件属性
    """
    import os

    def test1():
        print(os.path.exists('data/input'))
        print(os.path.isfile('data/input'))
        print(os.path.isdir('data'))
        print(os.path.realpath('data'))

        print(os.path.getsize('data'))
        print(os.path.getmtime('data'))


def chapter_5_13():
    """
    获取文件夹列表
    """
    import os

    def test1():
        names = os.listdir('data')

        filenames = [name for name in os.listdir('data')
                     if os.path.isfile(os.path.join('data', name))]

        dirnames = [name for name in os.listdir('data')
                    if os.path.isdir(os.path.join('data', name))]

        txtfiles = [name for name in os.listdir('data')
                    if name.endswith('.txt')]

