"""
2.1. Splitting Strings on Any of Multiple Delimiters
#   re.split()
???
"""
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
# print(re.split(r'[;,\s]\s*', line))

"""
2.2. Matching Text at the Start or End of a String
#   You need to check the start or end of a string for specific text patterns, such as filename
    extensions, URL schemes, and so on.
    str.startswith() / str.endswith()
"""
filename = 'spam.txt'
filename.startswith('fill:')
filename.endswith('.txt')
#   If you need to check against multiple choices, simply provide a tuple of possibilities to
#   startswith() or endswith().
filenames = ['makefile', 'test.c', 'test.cpp', 'test.py']
print([name for name in filenames if name.endswith(('.c', '.cpp', '.py'))])

