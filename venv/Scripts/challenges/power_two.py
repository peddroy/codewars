'''

Power of 2

https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python

'''

n = 2


def power_of_two(n):
    return [2 ** i for i in range(0, n + 1)]


print(power_of_two(n))
