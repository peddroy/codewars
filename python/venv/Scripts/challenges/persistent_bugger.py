'''

Persistent Bugger.

https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

'''

import math

n = 4


def persistence(n):
    count = 0
    while n > 9:
        n = math.prod([int(i) for i in str(n)])
        count += 1
    return count


print(persistence(n))
