'''
Sum The Strings

https://www.codewars.com/kata/5966e33c4e686b508700002d

'''

a = '5'
b = '9'


def sum_str(a, b):
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    return str(int(a) + int(b))


print(sum_str(a, b))
