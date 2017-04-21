'''
    rjust() / ljust() / center() justifies a string in a field of a given width by padding it with spaces.
        These methods do not write anything, they just return a new string. If the input string is too long, they don’t truncate
    it, but return it unchanged;

    zfill()
        pads a numeric string on the left with zeros. It understands about plus and minus signs.
    '12'.zfill(5)       ===>    '00012'
    '-3.14'.zfill(5)    ===>    '-003.14'

    format(*args, **kwargs)
        Perform a string formatting operation. The string on which this method is called can contain literal text or replacement
    fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name
    of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the
    corresponding argument.
    'The sum of 1 + 2 is {0}'.format(1+2)   ====>   'The sum of 1 + 2 is 3'
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
        ====>   'The story of Bill, Manfred, and Georg.'
    print('The value of PI is approximately {0:.3f}.'.format(math.pi))
        ====>   'The value of PI is approximately 3.142.'

'''
s = input("input: ")
# print(inStr)
