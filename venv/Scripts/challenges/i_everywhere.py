'''

I'm everywhere!

https://www.codewars.com/kata/6097a9f20d32c2000d0bdb98/train/python

'''

word = 'Python'


def i(word):
    vowel = []
    consonant = []

    if len(word) > 0:
        for i in word:
            if i in 'aeiouAEIOU':
                vowel.append(i)
            else:
                consonant.append(i)
        if len(vowel) >= len(consonant):
            return 'Invalid word'
        elif word[0].islower() or word[0] == 'I':
            return 'Invalid word'
        else:
            return f'i{word}'
    else:
        return 'Invalid word'


print(i(word))


'''

vowel = set("aeiouAEIOU").__contains__

def i(word):
    if not word or word[0].islower() or word[0] == 'I' or 2*sum(map(vowel, word)) >= len(word):
        return "Invalid word"
    return 'i' + word

'''

'''

def i(word):
    return f'i{word}' if word and word[0] != 'I' and word[0].isupper() and 2 * sum(1 for c in word if c in set('aeiouAEIOU')) < len(word) else 'Invalid word'

'''


'''

def less_vowels(word):
    vowels = sum(c in "aeiou" for c in word.lower())
    return len(word) - vowels > vowels


def i(word):
    return ( "i" + word
                if  not word.startswith("I")
                    and less_vowels(word)
                    and word[0] != word[0].lower()
                else "Invalid word" )

'''
