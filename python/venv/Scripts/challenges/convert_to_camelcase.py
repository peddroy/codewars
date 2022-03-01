# Convert string to camel case

text = 'text_are-done'

def to_camel_case(text):
    text = text.split('-')
    text = ' '.join(text)
    text = text.split('_')
    text = ' '.join(text)
    text = text.split(' ')
    text = ' '.join(text)
    splitted = text.split(' ')

    if text != '':
        # if splitted[0].islower():
        #     for i, valor in enumerate(splitted):
        #         if i > 0:
        #             splitted[i] = valor.replace(valor, valor.title())
        #     splitted = ''.join(splitted)
        #     return splitted
        # else:
            for i in (splitted[1:]):
                i = i.title()
                splitted[i] = i
                print(i)
            splitted = ''.join(splitted)
            return splitted
    else:
        return ''


print(to_camel_case(text))

# VERSION II
# text = 'job_to-be_done'
#
#
# def to_camel_case(text):
#     removed = text.replace('-', ' ').replace('_', ' ').split()
#
#     if len(removed) == 0:
#         return ''
#     else:
#         return removed[0] + ''.join([x.capitalize() for x in removed[1:]])
#
#
# print(to_camel_case(text))

