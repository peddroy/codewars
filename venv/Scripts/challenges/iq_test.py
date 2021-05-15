'''

IQ Test

https://www.codewars.com/kata/552c028c030765286c00007d

'''


numbers = ("2 4 6 8 11")


def iq_test(numbers):
    numbers = list(map(lambda n: int(n), numbers.split(' ')))
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]

    if len(even) == 1:
        return numbers.index(even[0]) + 1
    else:
        return numbers.index(odd[0]) + 1


print(iq_test(numbers))
