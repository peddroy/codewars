'''

Vowel Count

https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

'''


s = "ameixa"

v = ['a', 'e', 'i', 'o', 'u']


'''
PRIMEIRA RESOLUÇÃO

count = 0

for i in v:
    for l in s:
        if i == l:
            count += 1

print(count)

'''


def get_count(input_str):
    return list(map(lambda r: r in 'aeiou', s)).count(True)
