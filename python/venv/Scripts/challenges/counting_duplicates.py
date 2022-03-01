'''

Counting Duplicates

https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python


'''


text = 'abcdDDDeaa11'


def duplicate_count(text):
    text = text.lower()
    text = {i: text.count(i) for i in text}
    count = 0

    for i, j in text.items():
        if j > 1:
            count += 1

    return count


print(duplicate_count(text))
