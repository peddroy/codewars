'''

Returning Strings

https://www.codewars.com/kata/55a70521798b14d4750000a4

'''

name = 'Pedro'


def greet(name):

    greeting = 'Hello, <name> how are you doing today?'
    new_greeting = greeting.split()

    greeting = ' '.join(
        map(lambda x: x if x != '<name>' else name, new_greeting))

    return greeting


print(greet(name))
