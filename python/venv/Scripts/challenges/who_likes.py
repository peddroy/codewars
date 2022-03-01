'''
Who likes it?

https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

'''

names = ['Peter', 'Alex', 'Gabriel', 'Max', 'Alex',
         'Gabriel', 'Max', 'Alex', 'Gabriel', 'Max']


def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f"{''.join(names)} likes this"
    elif len(names) == 2:
        return f"{''.join(names[0])} and {''.join(names[1])} like this"
    elif len(names) == 3:
        return f"{''.join(names[0])}, {''.join(names[1])} and {''.join(names[2])} like this"
    else:
        return f"{''.join(names[0])}, {''.join(names[1])} and {len(names) - 2} others like this"


print(likes(names))
