'''

Gravity Flip

https://www.codewars.com/kata/5f70c883e10f9e0001c89673

'''

a = [3, 2, 1, 2]
d = 'L'


def flip(d, a):
    if d == 'R':
        a.sort()
    else:
        a.sort(reverse=True)
    return a


print(flip(d, a))
