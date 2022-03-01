'''

What's the real floor?

https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python

'''


n = -3


def get_real_floor(n):
    if n == 1:
        return 0
    elif 1 < n <= 13:
        return (n - 1)
    elif n > 13:
        return (n - 2)
    else:
        return n


print(get_real_floor(n))
