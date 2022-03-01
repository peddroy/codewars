'''
Find the first non-consecutive number

https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python

'''

arr = [1, 2, 3, 4, 5, 6, 7]


def first_non_consecutive(arr):
    count = arr[0]
    for i in arr:
        if i != count:
            return i
        count = i + 1


print(first_non_consecutive(numbers))
