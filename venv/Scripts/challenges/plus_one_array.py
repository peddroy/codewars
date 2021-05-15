'''

+1 Array

https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9

'''

arr = [1, 2, 9]


def up_array(arr):
    if not arr:
        return None
    elif [x for x in arr if x < 0]:
        return None
    elif [x for x in arr if x > 9]:
        return None
    else:
        arr = map(int, str(int(''.join([str(x) for x in arr])) + 1))
        return arr


print(list(up_array(arr)))
