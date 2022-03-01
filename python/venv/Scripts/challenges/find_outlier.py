n = [2, 4, 6, 8, 9, 10]

def find_outlier(n):
    n_impares = []
    n_pares = []
    for i in n:
        if i % 2 == 0:
            n_pares.append(i)
        else:
            n_impares.append(i)

    if len(n_impares) > 1:
        return n_pares[0]
    else:
        return n_impares[0]


print(find_outlier(n))

'''

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

'''