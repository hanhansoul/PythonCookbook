import re


def split_test():
    """
    re.split(pattern
    """
    print(re.split(r'\W+', 'Words,words,words.'))
    print(re.split(r'(\W+)', 'Words,words,words.'))
    print(re.split(r'\W+', 'Words,words,words.', 1))
    print(re.split(r'[a-f]+', '0a3B9', flags=re.IGNORECASE))


def displaymatch(match):
    if match is None:
        print(None)
    else:
        print('<Match:%r, groups=%r>' % (match.group(), match.groups()))


valid = re.compile(r'^[a2-9tjqk]{5}$')
displaymatch(valid.match('akt5q'))
displaymatch(valid.match('akt5e'))
displaymatch(valid.match('akt'))
displaymatch(valid.match('727ak'))

pair = re.compile(r'.*(.).*\1')
displaymatch(pair.match('717ak'))
