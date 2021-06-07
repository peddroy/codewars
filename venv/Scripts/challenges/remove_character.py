'''

Remove First and Last Character

https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python

'''

'''
s = 'Pe'


def remove_char(s):
    new_word = []
    if len(s) > 2:
        for i, j in enumerate(s):
            if i != 0:
                new_word.append(j)

        new_word.pop()

        new_word = ''.join(new_word)
        return new_word
    else:
        return ''


print(remove_char(s))

'''

s = 'cassr'


def remove_char2(s):
    return s[1: -1]


print(remove_char2(s))
