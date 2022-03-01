'''
Multiplication table for number

https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python

'''

# def multi_table(number):
#     return # good luck

number = 5


# def multi_table(number):
#     for i in range(1, 11):
#         result = i * number
#         print(f'{i} * {number} = {result}')


# multi_table(n)


def multi_table(number):
    line = []
    for i in range(1, 11):
        line.append(f'{i} * {number} = {i * number}')
    line = '\n'.join(line)
    return line


print(multi_table(number))
