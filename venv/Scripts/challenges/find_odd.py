'''

Find the odd int

https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

'''

# from collections import Counter

n = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]


# def find_it(seq):

#     n_set = set(seq)

#     for i in n_set:
#         count = 0
#         for j in n:
#             if i == j:
#                 count += 1

#         if count % 2 != 0:
#             max = i

#     return max


# print(find_it(n))

pessoa = {}

for i in n:
    print(i)
    pessoa = pessoa.update({.fromkeys(['numero'], i)})

print(pessoa)
