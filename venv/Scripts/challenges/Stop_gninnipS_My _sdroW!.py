print(f'Exercise - Stop gninnipS My sdroW!')

'''

def spin_words(sentence):
    sentence_split = sentence.split(' ')
    new_sentence = []

    for i in sentence_split:
        if len(i) >= 5:
            new_sentence.append(i.replace(i , i[::-1]))
        else:
            new_sentence.append(i)
        new_sentence_string = ' '.join(new_sentence)
    return new_sentence_string


print(spin_words('Hey fellow warriors'))

'''

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


texto = 'Samba cotia na casa da tia'
print(spin_words(texto))


texto = [x for x in texto.split(' ')]
print(texto)