n = 112341234

# def digital_root(n):
#     while n > 9:
#         new_n = 0
#
#         for i in str(n):
#             new_n = new_n + int(i)
#         n = new_n
#
#     return n

# print(digital_root(n))



def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
print(digital_root(n))


calculo = list(map(int, str(n)))
print(f'calcu {calculo}')


# iteravel e função

#
# inteiro = 12341234
#
# if inteiro < 10:
#     print(inteiro)
# else:
#     soma_digitos = sum(map(int, str(inteiro)))
#
# print(soma_digitos)

print(list(map(int(), str(int))))
