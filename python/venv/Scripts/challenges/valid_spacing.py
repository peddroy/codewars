print(f'Exercise - Valid Spacing!')

s = '  hello mana'

# def valid_spacing(s):
#     invalid_list = []
#     if s == '':
#         return True
#     elif s[0] == ' ':
#         return False
#     elif s[-1] == ' ':
#         return False
#     else:
#         for curr, next in zip(s, s[1:]):
#             if curr == ' ' and next == ' ':
#                 invalid_list.append('a')
#     if len(invalid_list) >= 1:
#         return False
#     else:
#         return True
#
# print(valid_spacing(s))

def valid_spacing(s):
    return s == ' '.join(s.split())

s_split = s.split()

print(s_split)

string = 'barata macarrão feijão'
usando_find = string.find('feijão')

print(f'aqui find {usando_find}')
