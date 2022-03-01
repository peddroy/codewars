'''
Remove exclamation marks

https://www.codewars.com/kata/57a0885cbb9944e24c00008e

'''

s = 'minha! string tem !'


def remove_exclamation_marks(s):
    return ''.join([elem for elem in s if elem != '!'])


print(remove_exclamation_marks(s))
