'''
Return Negative

https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python

'''

number = -663


def make_negative(number):
    if number > 0:
        number = number - number * 2
    return number


print(make_negative(number))
