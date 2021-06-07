'''

https://pt.stackoverflow.com/questions/120389/como-remover-caracteres-de-uma-string

'''

first_s = 'chocolate'
second_s = 'oca'

for i in second_s:
    if i in first_s:
        first_s = first_s.replace(i, '')
