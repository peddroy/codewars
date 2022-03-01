'''

Multiples of 3 or 5

https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

'''

number = 25


def solution(number):
    return sum([x for x in range(1, number) if x % 3 == 0 or x % 5 == 0])


print(solution(number))
